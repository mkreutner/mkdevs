#!make
include .env

# HELP
.PHONY: help

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

gen-pass: ## Generate an encrypt password from prompt
	@clear
	@./tools/system/gen_encrypt_password.sh

build: ## Build images
	@docker compose build
up: ## Start containers stack (dettached)
	@docker compose up -d
down: ## Stop containers stack 
	@docker compose down
destroy: ## Stop containers stack and remove volumes
	@docker compose down -v
ps: ## List all container
	@docker container ps -a

login-db: ## login on web container
	@docker compose exec -it db bash
login-nginx: ## login on nginx container
	@docker compose exec -it nginx bash

build-prod: ## [PROD] Build images
	@docker compose --file docker-compose-prod.yml build
up-prod: ## [PROD] Start containers stack (dettached)
	@docker compose --file docker-compose-prod.yml up -d
down-prod: ## [PROD] Stop containers stack 
	@docker compose --file docker-compose-prod.yml down
destroy-prod: ## [PROD] Stop containers stack and remove volumes
	@docker compose --file docker-compose-prod.yml down -v

runserver: ## run django project localy
	@cd ./src ; reset ; python manage.py runserver
psql: ## connect to database
	psql --username=mkdevs_user --host=localhost --port=5432 --dbname=mkdevs --password
