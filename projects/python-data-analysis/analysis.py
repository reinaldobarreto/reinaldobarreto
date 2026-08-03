from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "sales.csv"
OUT_PATH = BASE_DIR / "report.json"


def main() -> None:
    df = pd.read_csv(DATA_PATH)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["orders"] = pd.to_numeric(df["orders"], errors="coerce")
    df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")
    df = df.dropna(subset=["date", "channel", "orders", "revenue"])
    df["aov"] = np.where(df["orders"] > 0, df["revenue"] / df["orders"], 0.0)

    report = {
        "rows": int(df.shape[0]),
        "period": {
            "start": df["date"].min().date().isoformat(),
            "end": df["date"].max().date().isoformat(),
        },
        "kpis": {
            "orders_total": int(df["orders"].sum()),
            "revenue_total": float(df["revenue"].sum()),
            "aov_mean": float(df.loc[df["orders"] > 0, "aov"].mean()),
            "revenue_mean_per_day": float(df.groupby(df["date"].dt.date)["revenue"].sum().mean()),
        },
        "by_channel": (
            df.groupby("channel", as_index=False)
            .agg(orders=("orders", "sum"), revenue=("revenue", "sum"), aov=("aov", "mean"))
            .sort_values("revenue", ascending=False)
            .to_dict(orient="records")
        ),
    }

    OUT_PATH.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"report_written={OUT_PATH}")


if __name__ == "__main__":
    main()

