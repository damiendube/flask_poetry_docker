# Demo Flask app

It's been a while since I did my last python project.
Trying out my hands with a simple python application


Using, [Poetry](https://python-poetry.org) as my main build & dependency managment tool. Supporting both [Docker](https://www.docker.com) & [AWS EB](https://aws.amazon.com/elasticbeanstalk) deployement.


## Dev Mode
Install Dependencies in Virtual Environment

```sh
pyenv install
poetry install
```

Run

```sh
poetry run python application.py
```

## Docker

```sh
poetry run docker_build
poetry run docker_run
poetry run docker_stop
```

## AWS Elastic Beanstalk

```sh
poetry lock
poetry export -f requirements.txt > requirements.txt
eb deploy

```
