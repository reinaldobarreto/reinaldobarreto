## FastAPI CRUD API (template)

API REST simples e direta, ideal para demonstrar:

- FastAPI + OpenAPI/Swagger
- validação com Pydantic
- endpoints CRUD

### Rodando local

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Abra:
- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/redoc`

