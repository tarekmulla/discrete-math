'''Lambda function to generate Truth table'''
from json import dumps, loads
from layer import LOGGER
import layer

quotients = []
remainders = []


def lambda_handler(event, context):
    # pylint: disable=unused-argument
    '''generate truth table'''
    origin = ''
    try:
        # retrieve the parameters from the request
        origin = layer.get_origin(event['headers'])
        if event['body']:
            body_data = loads(event['body'])
            if 'proposition' in body_data and body_data['proposition']:
                proposition = str(body_data['proposition'])
        LOGGER.info(f'Received proposition: {proposition}')

    except Exception as ex:
        message = 'Error while generating Truth table'
        LOGGER.error(f'{message}, more info: {str(ex)}')
        return layer.http_response(500, dumps({'error': message}), origin)

    # return success response, with all items details
    return layer.http_response(200, dumps({
        'proposition': proposition
        }), origin)
