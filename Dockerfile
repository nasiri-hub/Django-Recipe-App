# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.13.1
FROM python:${PYTHON_VERSION}-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

ARG GID=10001 
RUN addgroup \
    --system \
    --gid "${GID}" \
    app

ARG UID=10001
RUN adduser \
    --system \
    --home "/home/app" \
    --shell "/bin/bash" \
    --uid "${UID}" \
    --ingroup app \
    app

RUN apt update  \
    && apt full-upgrade -y\
    && apt install -y --no-install-recommends \
    build-essential curl ca-certificates python3-venv \
    libpq5\
    python3-certbot-nginx\
    certbot\
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:0.5.25 /uv /uvx /bin/

COPY --chown=app:app pyproject.toml /app/

RUN uv pip install -r pyproject.toml --system

RUN chown -R app:app /app/

USER app

COPY --chown=app:app . /app/

EXPOSE 8000
