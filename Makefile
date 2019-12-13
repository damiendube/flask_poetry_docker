docker_build:
	docker build -t poetry_demo:latest .

docker_run:
	docker run -p 5000:5000 poetry_demo:latest 
