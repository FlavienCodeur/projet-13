FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

WORKDIR /app


COPY ./requirements.txt /app/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /app


CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
