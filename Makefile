brain-games:
	poetry run brain-games
lint:
	poetry run flake8 brain_games
restart: install build publish package-reinstall 
install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-reinstall:
	python3 -m pip install --force-reinstal --user dist/*.whl
package-install:
	python3 -m pip install --user dist/*.whl
