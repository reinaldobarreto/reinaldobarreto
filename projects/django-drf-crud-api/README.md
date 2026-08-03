## Django + DRF CRUD API (template)

API REST simples e direta, ideal para demonstrar:

- Django + Django REST Framework
- Model + Serializer + ViewSet + Router
- SQLite por padrão (local)

### Rodando local

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

API:
- `http://127.0.0.1:8000/api/tasks/`

