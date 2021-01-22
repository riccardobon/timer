virtualenv --python=python3.7 .vrtenv
source .vrtenv/bin/activate
python -m pip install nose rednose pytest coverage pytest-cov mypy flake8 pylint
