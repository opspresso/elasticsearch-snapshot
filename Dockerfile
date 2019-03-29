# Dockerfile

FROM python:3.7-alpine

RUN apk add --no-cache bash curl

RUN pip install boto3
RUN pip install requests
RUN pip install requests_aws4auth
RUN pip install slacker

COPY src /

ENTRYPOINT ["python", "/run.py"]
