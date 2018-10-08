.PHONY := test

test: .resolve
	python -m pytest --cov=./tests

lint: .resolve
	pylint --errors-only numeric_calc

.resolve: requirements.txt
	- pip install -r requirements.txt
	- touch .resolve
