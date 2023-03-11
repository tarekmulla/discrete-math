"""cognito operations file"""
import base64

import jwt
import requests

import app.config as CONFIG


def get_auth_header():
    """generate the encoded authentication header"""
    client_auth = f"{CONFIG.COGNITO_CLIENT_ID}:{CONFIG.COGNITO_CLIENT_SECRET}"
    auth_bytes = bytes(client_auth.encode("utf-8"))
    auth_header = f'Basic {base64.b64encode(auth_bytes).decode("utf-8")}'
    return auth_header


def send_exch_token_request(code: str):
    """send exchange token request to cognito"""
    url = CONFIG.GET_TOKEN_URL
    response = None
    auth_header = get_auth_header()
    header_type = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": auth_header,
    }
    body = {
        "code": code,
        "grant_type": "authorization_code",
        "client_id": CONFIG.COGNITO_CLIENT_ID,
        "client_secret": CONFIG.COGNITO_CLIENT_SECRET,
        "redirect_uri": CONFIG.CALLBACK_URL,
    }
    response = requests.post(url=url, data=body, headers=header_type, timeout=5)
    if response.status_code == 200:
        return response.json()
    return {}


def get_session_details(code: str):
    """Exchange cognito code with token"""
    session_details = send_exch_token_request(code)
    if "id_token" in session_details:
        id_token = session_details["id_token"]
        access_token = session_details["access_token"]
        user_details = jwt.decode(
            id_token, algorithms=["RS256"], options={"verify_signature": False}
        )
        return {"token": access_token, "username": user_details["email"]}
    return {}
