# pylint: disable=import-error
'''API utils file'''
import requests
import base64
import jwt
from os import environ
import ast


COGNITO_DOMAIN = environ['cognito_domain']
COGNITO_CLIENT_ID = environ['cognito_client_id']
COGNITO_CLIENT_SECRET = environ['cognito_client_secret']
CALLBACK_URLS = ast.literal_eval(environ['callback_urls'])


def get_session_details(code):
    '''Exchange cognito code with token'''
    url = f'https://{COGNITO_DOMAIN}/oauth2/token'
    response = None
    client_auth = f'{COGNITO_CLIENT_ID}:{COGNITO_CLIENT_SECRET}'.encode('utf-8')
    header_type = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Basic {base64.b64encode(bytes(client_auth)).decode("utf-8")}'
        }
    body = {
        'client_id': COGNITO_CLIENT_ID,
        'client_secret': COGNITO_CLIENT_SECRET,
        'code': code,
        'grant_type': 'authorization_code',
        'redirect_uri': CALLBACK_URLS[0]
    }
    response = requests.post(url=url,
                             data=body,
                             headers=header_type)
    session_details = response.json()
    id_token = session_details['id_token']
    access_token = session_details['access_token']
    user_details = jwt.decode(id_token, algorithms=["RS256"],
                              options={"verify_signature": False})
    return access_token, user_details['email']
