import os
import boto3
import requests

# from requests_aws4auth import AWS4Auth
from datetime import date, timedelta
from slacker import Slacker

region = os.environ.get('AWS_REGION', 'ap-northeast-2')

bucket = os.environ.get('AWS_BUCKET')

host = os.environ.get('ES_HOST')

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
    index = 'logstash-' + (date.today() - timedelta(40)).strftime("%Y.%m.%d")

    print('Remove index : %s' % index)

    try:
        url = host + index

        r = requests.delete(url)

        post_slack('Remove index : %s : %s' % (index, r.text))

    except KeyError as ex:
        post_slack('Environment variable %s not set.' % str(ex))


def remove_snapshot():
    snapshot = 'snapshot-' + (date.today() - timedelta(330)).strftime("%Y.%m.%d")

    print('Remove snapshot : %s/%s' % (bucket, snapshot))

    try:
        url = host + '_snapshot/' + bucket + '/' + snapshot

        r = requests.delete(url)

        post_slack('Remove snapshot : %s/%s : %s' % (bucket, snapshot, r.text))

    except KeyError as ex:
        post_slack('Environment variable %s not set.' % str(ex))


def take_snapshot():
    snapshot = 'snapshot-' + (date.today()).strftime("%Y.%m.%d")

    print('Take snapshot : %s/%s' % (bucket, snapshot))

    try:
        url = host + '_snapshot/' + bucket + '/' + snapshot

        # r = requests.put(url, auth=awsauth)
        r = requests.put(url)

        post_slack('Take snapshot : %s/%s : %s' % (bucket, snapshot, r.text))

    except KeyError as ex:
        post_slack('Environment variable %s not set.' % str(ex))


if __name__ == '__main__':
    # remove_index()

    # remove_snapshot()

    take_snapshot()
