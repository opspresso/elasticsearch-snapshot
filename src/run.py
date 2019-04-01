import os
import boto3
import requests

# from requests_aws4auth import AWS4Auth
from datetime import date, timedelta
from slacker import Slacker

region = os.environ.get('AWS_REGION', 'ap-northeast-2')

bucket = os.environ.get('AWS_BUCKET')

es_host = os.environ.get('ES_HOST')

index_prefix = os.environ.get('INDEX_PREFIX', 'logstash')
index_interval = os.environ.get('INDEX_INTERVAL', 40)

snapshot_prefix = os.environ.get('SNAPSHOT_PREFIX', 'snapshot')
snapshot_interval = os.environ.get('SNAPSHOT_INTERVAL', 365)

token = os.environ.get('SLACK_TOKEN')
channal = os.environ.get('SLACK_CHANNAL', '#sandbox')

if token != '':
    slack = Slacker(token)

# credentials = boto3.Session().get_credentials()
# awsauth = AWS4Auth(credentials.access_key, credentials.secret_key,
#                    region, 'es', session_token=credentials.token)

# Take snapshot


def post_slack(text):
    print(text)

    if token != '':
        slack.chat.post_message(channal, text)


def remove_index():
    index = index_prefix + '-' + (date.today() - timedelta(index_interval)).strftime("%Y.%m.%d")

    print('Remove %s : %s' % (index_prefix, index))

    try:
        url = es_host + index

        r = requests.delete(url)

        post_slack('Remove %s : %s : %s' % (index_prefix, index, r.text))

    except KeyError as ex:
        post_slack('Environment variable %s not set.' % str(ex))


def remove_snapshot():
    snapshot = snapshot_prefix + '-' + (date.today() - timedelta(snapshot_interval)).strftime("%Y.%m.%d")

    print('Remove %s : %s/%s' % (snapshot_prefix, bucket, snapshot))

    try:
        url = es_host + '_snapshot/' + bucket + '/' + snapshot

        r = requests.delete(url)

        post_slack('Remove %s : %s/%s : %s' % (snapshot_prefix, bucket, snapshot, r.text))

    except KeyError as ex:
        post_slack('Environment variable %s not set.' % str(ex))


def take_snapshot():
    snapshot = snapshot_prefix + '-' + (date.today()).strftime("%Y.%m.%d")

    print('Take %s : %s/%s' % (snapshot_prefix, bucket, snapshot))

    try:
        url = es_host + '_snapshot/' + bucket + '/' + snapshot

        # r = requests.put(url, auth=awsauth)
        r = requests.put(url)

        post_slack('Take %s : %s/%s : %s' % (snapshot_prefix, bucket, snapshot, r.text))

    except KeyError as ex:
        post_slack('Environment variable %s not set.' % str(ex))


if __name__ == '__main__':
    if bucket is None or bucket == '':
        raise ValueError('AWS_BUCKET')

    if es_host is None or es_host == '':
        raise ValueError('ES_HOST')

    # remove_index()

    # remove_snapshot()

    take_snapshot()
