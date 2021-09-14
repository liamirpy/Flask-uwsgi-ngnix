FROM tiangolo/uwsgi-nginx-flask:python3.8
ENV STATIC_URL /static
ENV STATIC_PATH /app/static
ENV NGINX_WORKER_PROCESSES auto
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY ./app /app
