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

tests:
	poetry run pytest --cov-report term:skip-covered tictactoe tests/

test-coverage:
	poetry run pytest --cov=tictactoe --cov-report xml tests/

.PHONY: tictactoe tests
