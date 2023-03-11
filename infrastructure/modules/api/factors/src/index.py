'''Lambda function to generate factors and check prime'''
from json import dumps, loads
from layer import LOGGER
import layer


def lambda_handler(event, context):
    # pylint: disable=unused-argument
    '''generate factors and check prime'''
    origin = ''
    try:
        # retrieve the parameters from the request
        origin = layer.get_origin(event['headers'])
        if event['body']:
            body_data = loads(event['body'])
            if 'number' in body_data and body_data['number']:
                number = int(body_data['number'])
        LOGGER.info(f'Received number: {number}')
        prime_factors = generate_prime_factors(number)
        factors = get_factors(number)

    except Exception as ex:
        message = 'Error while generating factors and checking prime'
        LOGGER.error(f'{message}, more info: {str(ex)}')
        return layer.http_response(500, dumps({'error': message}), origin)

    # return success response, with all items details
    return layer.http_response(200, dumps({
        "factors": str(factors),
        "prime_factors": str(prime_factors)
        }), origin)


def get_factors(num):
    """generate factors for specific number"""
    factors_set = set(
        factor for i in range(1, int(num**0.5) + 1) if num % i == 0
        for factor in (i, num//i)
    )
    factors_list = list(factors_set)
    factors_list.sort()
    return factors_list


def sieve_of_eratosthenes(N, s):
    '''create a boolean array "prime[0..n]" and initialize all entries in it as false'''
    prime = [False] * (N+1)
    # Initializing smallest factor equal to 2 for all the even numbers
    for i in range(2, N+1, 2):
        s[i] = 2
    # For odd numbers less than equal to n
    for i in range(3, N+1, 2):
        if not prime[i]:
            # s(i) for a prime is the number itself
            s[i] = i
            # For all multiples of current prime number
            for j in range(i, int(N / i) + 1, 2):
                if not prime[i*j]:
                    prime[i*j] = True
                    # i is the smallest prime factor for number "i*j"
                    s[i * j] = i


def generate_prime_factors(N):
    """function to generate prime factors and its power
    credit to: https://www.geeksforgeeks.org/print-all-prime-factors-and-their-powers/"""
    # s[i] is going to store smallest prime factor of i
    s = [0] * (N+1)

    # Filling values in s[] using sieve
    sieve_of_eratosthenes(N, s)
    curr = s[N]  # Current prime factor of N
    cnt = 1  # Power of current prime factor

    prime_factors = []
    while (N > 1):
        N //= s[N]
        # N is now N/s[N]. If new N also has smallest prime
        # factor as curr, increment power
        if (curr == s[N]):
            cnt += 1
            continue

        prime_factors.append((curr, cnt))
        # Update current prime factor as s[N] and initializing count as 1.
        curr = s[N]
        cnt = 1
    return prime_factors
