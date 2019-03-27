import os
import boto3
import requests

from datetime import date, timedelta
from requests_aws4auth import AWS4Auth
from slacker import Slacker

bucket = os.environ.get('AWS_BUCKET')
region = os.environ.get('AWS_REGION', 'ap-northeast-2')

host = os.environ.get('ES_HOST')

token = os.environ.get('SLACK_TOKEN')

# credentials = boto3.Session().get_credentials()
# awsauth = AWS4Auth(credentials.access_key, credentials.secret_key,
#                    region, 'es', session_token=credentials.token)

# Take snapshot

snapshot = 'snapshot-' + (date.today()).strftime("%Y.%m.%d")


def post_slack(channal, text):
    print(text)

    if token != '':
        slack = Slacker(token)
        slack.chat.post_message(channal, text)


def take_snapshot():
    post_slack('#sandbox', 'Take snapshot : %s/%s' % (bucket, snapshot))

    try:
        url = host + '_snapshot/' + bucket + '/' + snapshot

        # r = requests.put(url, auth=awsauth)
        r = requests.put(url)

        post_slack('#sandbox', 'Take snapshot : %s/%s : %s' %
                   (bucket, snapshot, r.text))

    except KeyError as ex:
        post_slack('#sandbox', 'Environment variable %s not set.' % str(ex))


if __name__ == '__main__':
    take_snapshot()
