run:
	@docker-compose -f ./docker-compose.yml up -d
stop:
	@docker-compose -f ./docker-compose.yml down
restart:
	@docker-compose -f ./docker-compose.yml down
	@docker-compose -f ./docker-compose.yml up -d
build:
	@docker build --platform=linux/amd64 -t discrete-math .
