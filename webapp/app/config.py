'''application configuration'''
from os import environ


WEBSITE_DOMAIN = environ["website_domain"]
ORIGIN = 'https://{WEBSITE_DOMAIN}'
API_ENDPOINT = f'https://api.{WEBSITE_DOMAIN}'
COGNITO_DOMAIN = f'cognito.{WEBSITE_DOMAIN}'
COGNITO_CLIENT_ID = environ['cognito_client_id']
COGNITO_CLIENT_SECRET = environ['cognito_client_secret']
CALLBACK_URL = environ['callback_url']
LOGOUT_URI = environ['logout_url']

LOGIN_URL = f'https://{COGNITO_DOMAIN}/oauth2/authorize?\
client_id={COGNITO_CLIENT_ID}&\
response_type=code&\
scope=aws.cognito.signin.user.admin+email+openid+phone+profile&\
redirect_uri={CALLBACK_URL}'
LOGOUT_URL = f'https://{COGNITO_DOMAIN}/logout?client_id={COGNITO_CLIENT_ID}&logout_uri={LOGOUT_URI}'
GET_TOKEN_URL = f'https://{COGNITO_DOMAIN}/oauth2/token'
