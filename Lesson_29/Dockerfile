FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install psycopg2-binary allure-pytest
ENTRYPOINT ["pytest", "--alluredir=allure-results"]