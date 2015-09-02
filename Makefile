.PHONY: run clean reload init

PROJECT_NAME=aol
PYTHON=python3
# make sure pg_config is in the path otherwise psycopg2 won't compile
export PATH:=.env/bin:/usr/pgsql-9.3/bin:$(PATH)


run: .env
	python manage.py runserver 0.0.0.0:8000

clean:
	find . -iname "*.pyc" -delete
	find . -iname "*.pyo" -delete
	find . -iname "__pycache__" -delete

reload: .env
	python manage.py migrate
	python manage.py collectstatic --noinput
	touch $(PROJECT_NAME)/wsgi.py

test:
	python manage.py test --keepdb && flake8 && isort -rc --diff --check-only $(PROJECT_NAME)

init:
	rm -rf .env
	$(MAKE) .env
	psql postgres -c "CREATE DATABASE $(PROJECT_NAME);"
	psql $(PROJECT_NAME) -c "CREATE EXTENSION postgis;"
	python manage.py migrate

.env: requirements.txt
	$(PYTHON) -m venv .env
	curl https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py | python
	pip install -r requirements.txt
