'''A lambda layer for all shared methods between lambda functions'''
import logging
from os import environ
from random import randint


# Create logger to record system events, will be used by other lambda functions
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


def http_response(code: int, body: str, origin: str) -> dict:
    '''Return http response with a code and body'''
    if code < 200 or code > 599:
        raise ValueError("Status code is invalid")
    return {
        'statusCode': code,
        'headers': generate_headers(origin),
        'body': body
        }


def generate_headers(origin):
    '''check the origin and generate http header'''
    web_domain = environ['WEB_DOMAIN']
    allowed_origins = [f'https://{web_domain}', web_domain]
    headers = {
        'Access-Control-Allow-Origin':
        origin if origin in allowed_origins
        else allowed_origins[0],
        'Content-Type': 'application/json',
        'Access-Control-Allow-Headers': 'Content-Type,Authorization',
        'Access-Control-Allow-Methods': 'OPTIONS,PUT,POST,GET',
        'Access-Control-Allow-Credentials': 'true'
    }
    return headers


def get_origin(headers: dict):
    '''retrieve the origin from the headers'''
    if 'origin' in headers:
        origin = headers['origin']
    else:
        raise ValueError("Expect origin in the header")
    return origin


def generate_numbers():
    '''generate 2 random numbers'''
    num_1 = randint(0, 999)
    num_2 = randint(0, 999)
    return num_1, num_2
