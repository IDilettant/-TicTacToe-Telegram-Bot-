install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 tictactoe

package-install:
	python3 -m pip install --user dist/*.whl

test:
	poetry run pytest tests

.PHONY: tictactoe tests
