#!/bin/bash

pytest -v --cov-config=.coveragerc --cov-report=html:toolbox_app/tests/coverage --cov=toolbox_app
python pytest_cov.py