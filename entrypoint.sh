#!/bin/sh

uv run alembic upgrade head

exec "$@"