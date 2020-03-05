FROM python:3.7.6-alpine3.10

COPY server.py /server.py
COPY requirements.txt /requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["gunicorn",  "-b", "0.0.0.0:5000", "server:app", "--loglevel info"]
