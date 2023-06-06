
.PHONY: docker
docker:
	docker compose build


.PHONY: docker-stop-all
docker-stop-all:
	docker compose down -v

.PHONY: docker-build
docker-build:
	docker compose up builder

.PHONY: docker-dev-server
docker-dev-server:
	docker compose up dev-server

.PHONY: docker-clean
docker-clean:
	docker compose up cleaner

.PHONY: docker-deploy
docker-deploy: docker-stop-all docker-clean docker-build
	DKR_GIT_NAME="$$(git config --get user.name)" \
	DKR_GIT_EMAIL="$$(git config --get user.email)" \
		docker compose up deployer
	git push --force origin gh-pages



.PHONY: build
build:
	./build.sh
