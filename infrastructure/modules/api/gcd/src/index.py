'''Lambda function to generate questions'''
from json import dumps, loads
from layer import LOGGER  # pylint: disable=import-error # type: ignore
import layer  # pylint: disable=import-error # type: ignore


def lambda_handler(event, context):
    # pylint: disable=unused-argument
    '''generate questions randomly'''
    origin = ''
    try:
        # retrieve the parameters from the request
        origin = layer.get_origin(event['headers'])
        if event['body']:
            body_data = loads(event['body'])
            if 'num1' in body_data and body_data['num1'] and 'num2' in body_data and body_data['num2']:
                num1 = max(int(body_data['num1']), int(body_data['num2']))
                num2 = min(int(body_data['num1']), int(body_data['num2']))
        LOGGER.info(f'Received parameters: {num1}, {num2}')
        gcd, x, y, steps = gcd_calc(num1, num2)
        lcm = (num1*num2)//gcd  # least common multiple

    except Exception as ex:  # pylint: disable=broad-exception-caught
        message = 'Error while calculating GCD'
        LOGGER.error(f'{message}, more info: {str(ex)}')
        return layer.http_response(500, dumps({'error': message}), origin)

    # return success response, with all items details
    return layer.http_response(200, dumps({
        'gcd': gcd,
        'lcm': lcm,
        'result': f'GCD of {num1} and {num2} is {gcd}',
        'steps': steps,
        'bezout': f'{gcd} = {x}({num1}) - {y}({num2})'
        }), origin)


def gcd_calc(a, b, steps_str='', x=0, prev_x=1, y=1, prev_y=0):
    '''calculate the GCD and Bézout's using the extended euclidean algorithm
    credit to: https://github.com/BaReinhard/Hacktoberfest-Mathematics/blob/master/algebra/bezout/python/bezout.py'''
    # 'a' has to be greater than 'b'
    if b > a:
        a, b = b, a

    # calculate the remainder of a/b
    remainder = a % b
    quotient = a // b

    steps_str += f'{a} = {quotient}({b})'

    # if remainder is 0, stop here : gcd found
    if remainder == 0:
        steps_str += ' <-- GCD'
        return b, x, y, steps_str
    else:
        steps_str += f' + {remainder}\n'

    # else, update x and y, and continue
    prev_x, prev_y, x, y = x, y, quotient*x + prev_x, quotient*y + prev_y
    return gcd_calc(b, remainder, steps_str, x, prev_x, y, prev_y)
