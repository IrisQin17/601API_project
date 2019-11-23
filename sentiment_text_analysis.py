
# Copyright 2019 Xushan Hu

# To install the latest published package dependency, execute the following:
#   pip install google-cloud-language

import sys

from google.cloud import language_v1
from google.cloud.language_v1 import enums
import six

def analyze_sentiment_from_twitter(file):
    f = open(file,'r',encoding='utf-8')
    data = f.read()
    client = language_v1.LanguageServiceClient()
    if isinstance(data, six.binary_type):
        data = data.decode('utf-8')
    type1 = enums.Document.Type.PLAIN_TEXT
    document = {'type': type1, 'content': data}
    request = client.analyze_sentiment(document)
    sentiment = request.document_sentiment
    return ('{}'.format(sentiment.score), '{}'.format(sentiment.magnitude))
    # print('Score: {}'.format(sentiment.score))
    # print('Magnitude: {}'.format(sentiment.magnitude))