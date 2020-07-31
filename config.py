
import tweepy
import logging
import os

logger = logging.getLogger()


def create_api():
    consumer_key = 'OQxgV4vKMRChM8C1EZWdTlFdJ'
    consumer_secret = 'uTkJga31g1IrQbw2XWKNjDXJZBDixmFajoTEpCrLY64LVgg4o0'
    access_token = '1379945563-0qxFJofXOgQwiHliJjhvLkO9vgghqEqOXoegpth'
    access_token_secret = 'iRZ2WyM4xqUgd9orUkGP3cxYCRfq7JMY38PS9ot55rVMa'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error('Error creating API', exc_info=True)
        raise e
    logger.info('API created')
    return api
