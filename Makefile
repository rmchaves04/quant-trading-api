init: build up
.PHONY: init

build:
	@docker-compose build --no-cache
.PHONY: build

up:
	@docker-compose up -d
.PHONY: up

clean:
	@docker-compose down --remove-orphans
.PHONY: clean

restart: clean build up
.PHONY: restart