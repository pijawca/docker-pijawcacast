up:
	docker-compose up

rm:
	sudo docker compose stop \
	&& docker rm $(docker ps -a -q) \
	&& docker rmi $(docker images -q) \
	&& rm -rf pgdata \