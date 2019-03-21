# Dockerfile

FROM python:3.7-alpine

RUN apk add --no-cache bash curl

RUN pip install boto3
RUN pip install requests
RUN pip install requests_aws4auth

COPY src /

ENTRYPOINT ["python", "/take-snapshot.py"]
