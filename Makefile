aws-eb-create-env:
	eb create my-env

aws-eb-deploy:
	poetry lock
	poetry export -f requirements.txt > requirements.txt
	eb deploy
