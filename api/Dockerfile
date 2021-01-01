FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /api/

RUN pip install pipenv
COPY Pipfile Pipfile.lock /api/
RUN pipenv install --system --dev

COPY . /api/