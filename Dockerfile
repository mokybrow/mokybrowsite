FROM python:3.11


WORKDIR /fastapi

COPY /pyproject.toml /fastapi

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .

CMD uvicorn api.main:make_app --reload