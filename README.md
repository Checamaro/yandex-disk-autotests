# Yandex Disk API autotests

## install

pip install -r requirements.txt

## access token
create .env with your personal access token:
YANDEX_TOKEN=<your_personal_access_token>

## run tests

pytest --alluredir=allure-results

## allure

allure serve allure-results