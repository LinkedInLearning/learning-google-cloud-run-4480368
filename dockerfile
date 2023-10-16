FROM python:latest
COPY .  /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV ORG_NAME "GCP_LERANING"
ENTRYPOINT ["python","run.py"]