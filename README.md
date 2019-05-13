# elasticsearch-snapshot

[![GitHub release](https://img.shields.io/github/release/opsnow-tools/elasticsearch-snapshot.svg)](https://github.com/opsnow-tools/elasticsearch-snapshot/releases)
[![CircleCI](https://circleci.com/gh/opsnow-tools/elasticsearch-snapshot.svg?style=svg)](https://circleci.com/gh/opsnow-tools/elasticsearch-snapshot)

[![DockerHub Badge](http://dockeri.co/image/opsnowtools/elasticsearch-snapshot)](https://hub.docker.com/r/opsnowtools/elasticsearch-snapshot/)

```bash
docker pull opsnowtools/elasticsearch-snapshot
```

## usage

```
export AWS_REGION=ap-northeast-2
export AWS_BUCKET=elasticsearch-snapshot

export ES_HOST=http://elasticsearch.domain.com/

export SNAPSHOT_ENABLE=false
export SNAPSHOT_PREFIX=snapshot

export REMOVE_INDICES_ENABLE=false
export REMOVE_INDICES_DELTA=40

export REMOVE_SNAPSHOT_ENABLE=false
export REMOVE_SNAPSHOT_DELTA=365

export SLACK_TOKEN=xoxb-0000-0000-xxxx
export SLACK_CHANNAL=#sandbox
```
