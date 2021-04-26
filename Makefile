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
	poetry run pytest -v --cov-report term:skip-covered tictactoe tests/

cover:
	poetry run pytest --cov=tictactoe --cov-report xml tests/

pre-commit:
	poetry run pre-commit run --all-files

complex:
	poetry run flake8 --max-cognitive-complexity=5 $(file)

mypy:
	poetry run mypy tictactoe

.PHONY: tictactoe tests mypy
