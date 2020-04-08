cleanup:
	rm -rf build && rm -rf dist && rm -rf .eggs && rm -rf flake8_keyword_arguments.egg-info

wheel:
	python3 setup.py sdist bdist_wheel

upload:
	twine upload dist/*

pypi: cleanup wheel upload cleanup

requirements:
	pip install -r requirements-dev.txt

test:
	pytest --cov=flake8_keyword_arguments --cov-fail-under 100

coverage-collect:
	coverage run -m pytest

coverage-report:
	coverage html

coverage: coverage-collect coverage-report

mypy:
	mypy .

flake8:
	flake8 ./

isort:
	isort -y

check: isort flake8 mypy test
