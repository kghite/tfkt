# Development

devel-install:
	pip install -r requirements.txt -r deploy/develop/requirements.txt

devel-tidy:
	tidy --indent-spaces 2 --tidy-mark no templates/*

devel-format:
	black .
	isort .
	flake8 . --max-line-length=127

devel-makemigrations:
	python manage.py makemigrations --settings=tfkt.settings.development
	python manage.py migrate --settings=tfkt.settings.development

devel-server:
	python manage.py runserver --settings=tfkt.settings.development

devel-up:
	docker compose up


# Production

install:
	pip install -r deploy/requirements.txt

check-deploy:
	python manage.py check --deploy