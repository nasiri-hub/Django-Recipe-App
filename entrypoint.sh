#!/bin/bash

# Apply database makemigrations
# echo "Apply database makemigrations"
# python3 manage.py makemigrations core
# python3 manage.py migrate core

# # Apply database migrations
# echo "Apply database migrations"
# python3 manage.py migrate 

# Start server
echo "Starting server"
python3 manage.py runserver 0.0.0.0:8000