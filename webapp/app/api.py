# pylint: disable=import-error
'''API utils file'''
import json
from enum import Enum
import requests
from app.question import questionCls
from flask import current_app


API_ENDPOINT = "https://discrete-math-api.rmit.mulla.au"


class Request(Enum):
    '''reuqests type'''
    GET = 0
    POST = 1
    DELETE = 2


class Trigger(Enum):
    '''terraform trigger type on a question'''
    APPLY = 'apply'
    DESTROY = 'destroy'


def send_request(req_type: Request, path, data: dict = None):
    '''Send request to the API'''
    url = f'{API_ENDPOINT}{path}/'
    error_message = ''
    response = None
    header_type = {
        'Content-Type': 'application/json',
        'origin': 'https://discrete-math.rmit.mulla.au'
        }
    try:
        if req_type == Request.GET:
            response = requests.get(url,
                                    data=json.dumps(data),
                                    headers=header_type)
            return response
        elif req_type == Request.POST:
            response = requests.post(url=url,
                                     data=json.dumps(data),
                                     headers=header_type)
        elif req_type == Request.DELETE:
            response = requests.delete(url=url,
                                       data=json.dumps(data),
                                       headers=header_type)
    except requests.ConnectionError as ex:
        error_message = f'Connection error! more info {str(ex)}'
    except requests.Timeout as ex:
        error_message = f'Timeout! more info {str(ex)}'
    except requests.RequestException as ex:
        error_message = f'An error happened, more info {str(ex)}'

    if error_message:
        # Check the docker log to find what is the issue
        current_app.logger.error(error_message)
    return response


def get_request(path, data: dict):
    '''Send GET request to the API'''
    response = send_request(Request.GET, path, data)
    if response and response.status_code == 200:
        return response.json()
    else:
        return {}


def post_request(path, data: dict):
    '''Send POST request to the API'''
    response = send_request(Request.POST, path, data)
    if response and response.status_code == 200:
        return True
    else:
        return False


def delete_request(path, data: dict):
    '''Send DELETE request to the API'''
    response = send_request(Request.DELETE, path, data)
    if response and response.status_code == 200:
        return True
    else:
        return False


def generate_questions() -> list[questionCls]:
    """get auto-generated questions from the API"""
    response = get_request('/question', {
        'question_type': 'LSM',
        'question_number': '3'
        })

    if response:
        questions = []
        questions_response = response['questions']
        for item in questions_response:
            question = questionCls.load(item)
            questions.append(question)
        return questions
    else:
        return None
