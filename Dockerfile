FROM python:3.10


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN mkdir /app
WORKDIR /app


COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


COPY . /app/


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "library.wsgi:application"]