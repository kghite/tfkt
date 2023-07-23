# Development

devel-install:
	pip install -r requirements.txt -r develop/requirements.txt

devel-server:
	python manage.py runserver --settings=tracer.settings.development


# Production

install:
	pip install -r requirements.txt

check-deploy:
	python manage.py check --deploy