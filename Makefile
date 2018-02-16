setup:
	python3 -m venv ~/.recommendations

install:
	pip install -r requirements.txt

lint:
	pylint --disable=R,C *.py

run-basic-example:
	python ext/basic_usage.py
