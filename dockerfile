FROM python:3.12


WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY ./ /app/

RUN chmod a+x docker/*.sh

#WORKDIR backend

#CMD gunicorn main:main_app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000