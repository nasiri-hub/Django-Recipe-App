build:
	docker compose up --build -d --remove-orphans

up:
	docker compose up -d --remove-orphans

down:
	docker compose down

down-v:
	docker compose down -v

makemigrations:
	docker compose run --rm api python3 manage.py makemigrations

migrate:
	docker compose run --rm api python3 manage.py migrate

collectstatic:
	docker compose run --rm api python3 manage.py collectstatic --no-input

superuser:
	docker compose run --rm api python3 manage.py createsuperuser 

logs:
	docker compose logs