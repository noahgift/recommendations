setup:
	python3 -m venv ~/.recommendations

install:
	pip install --upgrade pip
	pip install --upgrade --force-reinstall -r requirements.txt
	python -m spacy download en

lint:
	pylint --disable=R,C *.py

run-basic-example:
	python ext/basic_usage.py
