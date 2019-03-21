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

yesterday = date.today() - timedelta(1)

snapshot = 'logstash-' + yesterday.strftime("%Y.%m.%d")

url = host + '_snapshot/' + bucket + '/' + snapshot

print('Take snapshot : ' + bucket + '/' + snapshot)

# r = requests.put(url, auth=awsauth)
r = requests.put(url)

print(r.text)

if token != '':
    slack = Slacker(token)
    slack.chat.post_message('#sandbox', 'Take snapshot : ' + bucket + '/' + snapshot)
