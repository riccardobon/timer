#!/bin/bash

rm .htmlcov/* .coverage -f
pytest -v --cov --cov-report=html timer_module/ test/

exit 0
