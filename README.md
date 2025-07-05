# Proyecto Django Listo - Gestión de Eventos

Este proyecto ya viene configurado con:

- Django
- DRF
- Modelo `Evento`
- Serializador
- API funcionando en `/api/eventos/`

## Pasos para ejecutar

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
