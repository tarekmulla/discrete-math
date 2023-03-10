"""API utils file"""
import json
from enum import Enum

import requests
from flask import current_app, session

import app.config as CONFIG
from app.classes.factors import FactorsCls
from app.classes.pair import PairCls
from app.classes.proposition import PropositionCls
from app.classes.question import QuestionCls


class Request(Enum):
    """reuqests type"""

    GET = 0
    POST = 1
    DELETE = 2


class Trigger(Enum):
    """terraform trigger type on a question"""

    APPLY = "apply"
    DESTROY = "destroy"


def send_request(req_type: Request, path: str, data: dict, token):
    """Send request to the API"""
    url = f'{CONFIG.API_ENDPOINT.strip("/")}/{path.strip("/")}/'
    error_message = ""
    response = requests.Response()
    header_type = {
        "Content-Type": "application/json",
        "origin": f"{CONFIG.ORIGIN}",
        "Authorization": f"{token}",
    }
    try:
        if req_type == Request.GET:
            response = requests.get(
                url, data=json.dumps(data), headers=header_type, timeout=5
            )
        elif req_type == Request.POST:
            response = requests.post(
                url=url, data=json.dumps(data), headers=header_type, timeout=5
            )
        elif req_type == Request.DELETE:
            response = requests.delete(
                url=url, data=json.dumps(data), headers=header_type, timeout=5
            )
    except requests.ConnectionError as ex:
        error_message = f"Connection error! more info {str(ex)}"
    except requests.Timeout as ex:
        error_message = f"Timeout! more info {str(ex)}"
    except requests.RequestException as ex:
        error_message = f"An error happened, more info {str(ex)}"

    if error_message:
        # Check the docker log to find what is the issue
        current_app.logger.error(error_message)
    elif response.status_code == 401:  # token expired
        current_app.logger.error("token expired")
        session.pop("token", default=None)
        # TODO: renew token
    return response


def get_request(path, data: dict, token):
    """Send GET request to the API"""
    response = send_request(Request.GET, path, data, token)
    if response and response.status_code == 200:
        return response.json()
    return False


def post_request(path, data: dict, token):
    """Send POST request to the API"""
    response = send_request(Request.POST, path, data, token)
    if response and response.status_code == 200:
        return True
    return False


def delete_request(path, data: dict, token):
    """Send DELETE request to the API"""
    response = send_request(Request.DELETE, path, data, token)
    if response and response.status_code == 200:
        return True
    return False


def generate_questions(token) -> list[QuestionCls]:
    """get auto-generated questions from the API"""
    response = get_request(
        "/question", {"question_type": "LSM", "question_number": "3"}, token
    )

    if response:
        questions = []
        questions_response = response["questions"]
        for item in questions_response:
            question = QuestionCls.load(item)
            questions.append(question)
        return questions
    return []


def get_factors(num_factors: FactorsCls, token) -> bool:
    """get the number factors from the API"""
    response = get_request("/module/factors", {"number": num_factors.number}, token)
    if response:
        num_factors.set_factors(response["factors"])
        num_factors.set_prime_factors(response["prime_factors"])
        return True
    return False


def calculate_gcd(pair: PairCls, token) -> bool:
    """calculate the GCD and LCM"""
    response = get_request(
        "module/gcd", {"num1": pair.number1, "num2": pair.number2}, token
    )
    if response:
        pair.gcd = int(response["gcd"])
        pair.lcm = int(response["lcm"])
        pair.bezout_x = int(response["bezout_x"])
        pair.bezout_y = int(response["bezout_y"])
        pair.set_euclidean_steps(response["euclidean_steps"])
        return True
    return False


def generate_truth_table(proposition: PropositionCls, token) -> bool:
    """get the truth table from the API"""
    response = get_request(
        "module/proposition", {"proposition": proposition.prop_exp}, token
    )
    current_app.logger.info(response)
    if response:
        proposition.prop_type = str(response["type"])
        proposition.set_truth_table(response["table"])
        return True
    return False
