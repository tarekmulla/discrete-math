'''Lambda function to generate empty response for options method'''
from json import dumps
from layer import LOGGER
import layer


def lambda_handler(event, context):
    # pylint: disable=unused-argument
    '''generate empty response for options method'''
    try:
        # retrieve the origin from the request header
        origin = layer.get_origin(event['headers'])
        LOGGER.info(f'Request origin: {origin}')
    except Exception as ex:
        message = 'Error while retrieving origin'
        LOGGER.error(f'{message}, more info: {str(ex)}')
        return layer.http_response(500, dumps({'error': message}), origin)

    # return success response, with all items details
    return layer.http_response(204, "", origin)
