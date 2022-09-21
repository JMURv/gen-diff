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


pytest:
	poetry run pytest


coverage:
	poetry run pytest --cov=gendiff --cov-report xml


json_test:
	poetry run gendiff gendiff/tests/fixture/file1.json gendiff/tests/fixture/file2.json


yml_test:
	poetry run gendiff gendiff/tests/fixture/file1.yml gendiff/tests/fixture/file2.yml

json_test_rec:
	poetry run gendiff gendiff/tests/fixture/recursive/file1.json gendiff/tests/fixture/recursive/file2.json


#git_hub_make
a:
	git add .

p:
	git push