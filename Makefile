install:
	poetry install

brain-games:
	poetry run brain-games
restart: build publish package-install 
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
package-reinstall:
	python3 -m pip install --force-reinstal --user dist/*.whl
