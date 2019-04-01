# elasticsearch-snapshot

[![Docker Repository on Quay](https://quay.io/repository/opsnow-tools/elasticsearch-snapshot/status "Docker Repository on Quay")](https://quay.io/repository/opsnow-tools/elasticsearch-snapshot)

## usage

```
docker pull quay.io/opsnow-tools/elasticsearch-snapshot

export AWS_REGION=ap-northeast-2
export AWS_BUCKET=elasticsearch-snapshot

export ES_HOST=http://elasticsearch.domain.com/

export INDEX_PREFIX=logstash
export INDEX_INTERVAL=40

export SNAPSHOT_PREFIX=snapshot
export SNAPSHOT_INTERVAL=365

export SLACK_TOKEN=xoxb-0000-0000-xxxx
export SLACK_CHANNAL=#sandbox
```
