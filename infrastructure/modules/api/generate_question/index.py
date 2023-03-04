'''Lambda function to generate questions'''
from json import dumps, loads
from enum import Enum
from layer import LOGGER  # pylint: disable=import-error # type: ignore
import layer  # pylint: disable=import-error # type: ignore


class QuestionType(Enum):
    '''questions type'''
    GCD = 0
    LSM = 1


def lambda_handler(event, context):
    # pylint: disable=unused-argument
    '''generate questions randomly'''
    try:
        # retrieve the parameters from the request
        question_type = None
        question_number = 0
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
                questions.append({"question": "GCD question"})
            elif question_type == QuestionType.LSM:
                questions.append({"question": "LSM question"})
    except Exception as ex:  # pylint: disable=broad-exception-caught
        message = 'Error while generating questions'
        LOGGER.error(f'{message}, more info: {str(ex)}')
        return layer.http_response(500, dumps({'error': message}))

    # return success response, with all items details
    return layer.http_response(200, dumps({
        'questions': questions
        }))
