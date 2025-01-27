#!/bin/bash

# Apply database makemigrations
# echo "Apply database makemigrations"
# python3 manage.py makemigrations 

# Apply database migrations
echo "Apply database migrations"
python3 manage.py migrate 

# Collect all static files to the root directory
python manage.py collectstatic --no-input

# Start server
echo "Starting server"
# python3 manage.py runserver 0.0.0.0:8000
gunicorn recipe_api.wsgi:application --bind 0.0.0.0:8000