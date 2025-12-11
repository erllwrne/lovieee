#!/usr/bin/env bash
# Exit on any error
set -o errexit

# Upgrade pip first (helps with dependencies like Pillow)
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate
