up:
	docker-compose -f docker-compose.yml up --force-recreate

rm:
	docker-compose stop \
	&& docker-compose down --rm all \
	&& sudo rm -rf pgdata/

build:
	clear \
	&& sudo docker-compose stop \
	&& docker-compose down --rmi all \
	&& docker volume prune \
	&& rm -rf pgdata/ \
	&& docker-compose -f docker-compose.yml up --build