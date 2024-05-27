.PHONY: build-task-executor generate-migrations

build-task-executor:
	@echo "Building Tasks Executor"
	cd task-executor && docker build -t task-executor .

generate-migrations:
	@echo "Generate migrations"
	docker-compose run backend alembic revision --autogenerate -m "$(message)"
