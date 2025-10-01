#!/usr/bin/env bash
set -e

echo "Collectstatic..."
python manage.py collectstatic --noinput

echo "Migrate DB..."
python manage.py migrate --noinput

echo "Done build.sh"
