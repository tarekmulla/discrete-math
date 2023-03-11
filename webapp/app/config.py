"""application configuration"""
from os import getenv

WEBSITE_DOMAIN = getenv("website_domain", "localhost")
ORIGIN = "https://{WEBSITE_DOMAIN}"
API_ENDPOINT = f"https://api.{WEBSITE_DOMAIN}"
COGNITO_DOMAIN = f"cognito.{WEBSITE_DOMAIN}"
COGNITO_CLIENT_ID = getenv("cognito_client_id", "")
COGNITO_CLIENT_SECRET = getenv("cognito_client_secret", "")
CALLBACK_URL = getenv("callback_url", "http://localhost/login")
LOGOUT_URI = getenv("logout_url", "http://localhost")

LOGIN_URL = f"https://{COGNITO_DOMAIN}/oauth2/authorize?\
client_id={COGNITO_CLIENT_ID}&\
response_type=code&\
scope=aws.cognito.signin.user.admin+email+openid+phone+profile&\
redirect_uri={CALLBACK_URL}"
LOGOUT_URL = f"https://{COGNITO_DOMAIN}/logout?client_id={COGNITO_CLIENT_ID}&logout_uri={LOGOUT_URI}"
GET_TOKEN_URL = f"https://{COGNITO_DOMAIN}/oauth2/token"
