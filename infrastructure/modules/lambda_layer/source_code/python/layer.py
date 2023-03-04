'''A lambda layer for all shared methods between lambda functions'''
import logging

# Create logger to record system events, will be used by other lambda functions
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


def http_response(code: int, body: str) -> dict:
    '''Return http response with a code and body'''
    if code < 200 or code > 599:
        raise ValueError("Status code is invalid")
    return {
        'statusCode': code,
        'headers': {'Content-Type': 'application/json'},
        'body': body
        }
