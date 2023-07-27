FROM python:3.11


WORKDIR /fastapi_app

COPY /pyproject.toml /fastapi

RUN pip3 install poetry==1.5.1
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .


WORKDIR api

CMD gunicorn api.main:make_app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000