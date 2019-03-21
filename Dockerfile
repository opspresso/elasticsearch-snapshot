# Dockerfile

FROM 3.7-alpine

RUN apk add --no-cache bash curl

COPY src /

ENTRYPOINT ["python", "/take-snapshot.py"]
