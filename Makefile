install:
	poetry install


build:
	poetry build


help:
	poetry run gendiff -h

pt:
	poetry run gendiff gendiff/tests/fixture/file1.json gendiff/tests/fixture/file2.json


publish:
	poetry publish --dry-run


package-install:
	python3 -m pip install --user --force dist/*.whl


make lint:
	poetry run flake8 gendiff

pytest:
	poetry run pytest

#git_hub_make
a:
	git add .

p:
	git push