.PHONY := test

test: resolve
	python -m pytest tests

lint: resolve
	pylint --errors-only numeric_calc

resolve:
	- pip install -r requirements.txt
	- touch resolve
