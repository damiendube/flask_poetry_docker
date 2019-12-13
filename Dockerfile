FROM python:3.7-alpine


ARG YOUR_ENV

ENV YOUR_ENV=${YOUR_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.0 \
  FLASK_APP=/code/demo/__init__.py

# install psycopg2 dependencies
RUN apk upgrade --update
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev

# System deps:
RUN pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
WORKDIR /code
COPY poetry.lock pyproject.toml /code/

# Project initialization:
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-ansi

# Creating folders, and files for a project:
COPY . /code

EXPOSE 5000
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5000", "wsgi"]