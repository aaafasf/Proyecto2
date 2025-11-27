build:
	docker build -t manchasimg:2.0.1 .

deploy:
	docker stack deploy --with-registry-auth -c stack.yml manchas

rm:
	docker stack rm manchas