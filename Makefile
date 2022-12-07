start:
	poetry run flask --app hexlet_flask_example/example --debug run

build:
	poetry build

publish:
	poetry publish --dry-run

package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall