# Development

devel-install:
	pip install -r requirements.txt -r develop/requirements.txt

devel-makemigrations:
	python manage.py makemigrations --settings=tracer.settings.development
	python manage.py migrate --settings=tracer.settings.development

devel-server:
	python manage.py runserver --settings=tracer.settings.development


# Production

install:
	pip install -r requirements.txt

check-deploy:
	python manage.py check --deploy