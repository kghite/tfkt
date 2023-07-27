# Development

devel-install:
	pip install -r requirements.txt -r develop/requirements.txt

devel-tidy:
	tidy -indent --indent-spaces 2 -quiet --tidy-mark no templates/*

devel-makemigrations:
	python manage.py makemigrations --settings=tfkt.settings.development
	python manage.py migrate --settings=tfkt.settings.development

devel-server:
	python manage.py runserver --settings=tfkt.settings.development


# Production

install:
	pip install -r requirements.txt

check-deploy:
	python manage.py check --deploy