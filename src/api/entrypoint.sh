#!/bin/sh

set -e

echo "${0}: running migrations."
python3 manage.py migrate --noinput
# echo "${0}: running i18n"
# django-admin compilemessages

exec "$@"

