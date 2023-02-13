python manage.py collectstatic --noinput
python manage.py migrate
gunicorn payment.wsgi:application --bind 0:8000
