FROM python:3.11-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN echo "Acquire::Check-Valid-Until \"false\";\nAcquire::Check-Date \"false\";" | cat > /etc/apt/apt.conf.d/10no--check-valid-until

RUN apt-get update

RUN pip install -U pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --dev --system --deploy --ignore-pipfile

COPY . . 

ENTRYPOINT [ "gunicorn", "config.wsgi" ]