build:
	docker compose -f compose.yaml up --build -d --remove-orphans

up:
	docker compose -f compose.yaml up -d

down:
	docker compose -f compose.yaml down

down-v:
	docker compose -f compose.yaml down -v

makemigrations:
	docker compose -f compose.yaml run --remove-orphans api python3 manage.py makemigrations

migrate:
	docker compose -f compose.yaml run --remove-orphans api python3 manage.py migrate

collectstatic:
	docker compose -f compose.yaml run --remove-orphans api python3 manage.py collectstatic --no-input

superuser:
	docker compose -f compose.yaml run --remove-orphans api python3 manage.py createsuperuser 

logs:
	docker compose logs