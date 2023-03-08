'''Lambda function to generate questions'''
from json import dumps, loads
from enum import Enum
from layer import LOGGER  # pylint: disable=import-error # type: ignore
import layer  # pylint: disable=import-error # type: ignore
import pandas as pd


class QuestionType(Enum):
    '''questions type'''
    GCD = 0
    LSM = 1


def lambda_handler(event, context):
    # pylint: disable=unused-argument
    '''generate questions randomly'''
    origin = ''
    try:
        # retrieve the parameters from the request
        origin = layer.get_origin(event['headers'])
        question_type = None
        question_number = 0
        data = {
            "calories": [420, 380, 390],
            "duration": [50, 40, 45]
        }

        # load data into a DataFrame object:
        panda_test_df = pd.DataFrame(data)

        if event['body']:
            body_data = loads(event['body'])
            if 'question_type' in body_data and body_data['question_type']:
                question_type = QuestionType[body_data['question_type']]
            if 'question_number' in body_data and body_data['question_number']:
                question_number = int(body_data['question_number'])
        LOGGER.info(f'Received parameters: {question_type}, {question_number}')
        questions = []
        for _ in range(question_number):
            if question_type == QuestionType.GCD:
                questions.append({"question": f"GCD {panda_test_df} question"})
            elif question_type == QuestionType.LSM:
                questions.append({"question": f"LSM {panda_test_df} question"})
    except Exception as ex:  # pylint: disable=broad-exception-caught
        message = 'Error while generating questions'
        LOGGER.error(f'{message}, more info: {str(ex)}')
        return layer.http_response(500, dumps({'error': message}), origin)

    # return success response, with all items details
    return layer.http_response(200, dumps({
        'questions': questions
        }), origin)
