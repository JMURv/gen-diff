install:
	poetry install


build:
	poetry build


help:
	poetry run gendiff -h


publish:
	poetry publish --dry-run


package-install:
	python3 -m pip install --user --force dist/*.whl


make lint:
	poetry run flake8 gendiff


test:
	poetry run pytest


test-vv:
	poetry run pytest -vv


test-cov:
	poetry run pytest --cov=gendiff --cov-report xml


test-coverage:
	poetry run pytest --cov-report term-missing --cov=gendiff


json_test:
	poetry run gendiff gendiff/tests/fixtures/file1_plane.json gendiff/tests/fixtures/file2_plane.json


json_test_rec:
	poetry run gendiff gendiff/tests/fixtures/file1.json gendiff/tests/fixtures/file2.json

yml_test_plain:
	poetry run gendiff --format plain gendiff/tests/fixtures/file1.yml gendiff/tests/fixtures/file2.yml

json_format:
	poetry run gendiff --format json gendiff/tests/fixtures/nested/yml/file1.yml gendiff/tests/fixtures/nested/yml/file2.yml



#git_hub_make
a:
	git add .

p:
	git push