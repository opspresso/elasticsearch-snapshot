# elasticsearch-snapshot

[![GitHub Actions status](https://github.com/opspresso/elasticsearch-snapshot/workflows/Build-Push/badge.svg)](https://github.com/opspresso/elasticsearch-snapshot/actions)
[![GitHub Releases](https://img.shields.io/github/release/opspresso/elasticsearch-snapshot.svg)](https://github.com/opspresso/elasticsearch-snapshot/releases)

[![DockerHub Badge](http://dockeri.co/image/opspresso/elasticsearch-snapshot)](https://hub.docker.com/r/opspresso/elasticsearch-snapshot/)

```bash
docker pull opspresso/elasticsearch-snapshot
```

## usage

```bash
export AWS_REGION=ap-northeast-2
export AWS_BUCKET=elasticsearch-snapshot

export ES_HOST=http://elasticsearch.domain.com/

export SNAPSHOT_ENABLE=false
export SNAPSHOT_PREFIX=snapshot

export REMOVE_INDICES_ENABLE=false
export REMOVE_INDICES_DELTA=40

export REMOVE_SNAPSHOT_ENABLE=false
export REMOVE_SNAPSHOT_DELTA=365

export SLACK_TOKEN=""
export SLACK_CHANNAL="#sandbox"
```

## ConfigMap

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: elasticsearch-snapshot
data:
  AWS_REGION: ap-northeast-2
  AWS_BUCKET: elasticsearch-snapshot
  ES_HOST: http://elasticsearch.domain.com/
  SNAPSHOT_ENABLE: "true"
  SNAPSHOT_PREFIX: "snapshot"
  REMOVE_INDICES_ENABLE: "false"
  REMOVE_INDICES_DELTA: "40"
  REMOVE_SNAPSHOT_ENABLE: "false"
  REMOVE_SNAPSHOT_DELTA: "365"
  SLACK_TOKEN: ""
  SLACK_CHANNAL: "#sandbox"
```
