import "./globals.css";

import type { ReactNode } from "react";


export const metadata = {
  title: "Python Backend Portfolio",
  description: "FastAPI, Django, SQL, Automation and Data Analytics"
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="pt-BR">
      <body>{children}</body>
    </html>
  );
}

