import os
import boto3
import requests
import re

# from requests_aws4auth import AWS4Auth
from datetime import date, timedelta, datetime
from slacker import Slacker

region = os.environ.get('AWS_REGION', 'ap-northeast-2')

bucket = os.environ.get('AWS_BUCKET')

es_host = os.environ.get('ES_HOST')


def indices():
    past = date.today() - timedelta(20)

    url = es_host + '_cat/indices?format=json'
    json = requests.get(url).json()

    for item in json:
        match = re.search(r'\d{4}.\d{2}.\d{2}', item['index'])
        if match:
            s = match.group()
            d = datetime.strptime(s[0:4]+s[5:7]+s[8:10], '%Y%m%d').date()
            if d < past:
                print('%s %s' % (d, item['index']))


if __name__ == '__main__':
    if bucket is None or bucket == '':
        raise ValueError('AWS_BUCKET')

    if es_host is None or es_host == '':
        raise ValueError('ES_HOST')

    indices()
