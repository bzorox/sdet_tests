# SDET Test Task

## Setup
pip install selenium pytest allure-pytest

## Run tests
pytest --alluredir=allure-results
allure serve allure-results

## Positive test case
Fill all fields -> Submit -> Alert appears

## Negative test case
Missing required fields -> No alert
