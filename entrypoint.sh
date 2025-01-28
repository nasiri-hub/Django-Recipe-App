#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python3 manage.py migrate 

# Collect all static files to the root directory
python3 manage.py collectstatic --no-input

# Start server
echo "Starting server"
gunicorn recipe_api.wsgi:application --bind 0.0.0.0:8000