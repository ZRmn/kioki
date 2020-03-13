from algorithms import *
import random


def generate_public_exponent(phi):
    e = random.randrange(1, phi)
    d = euclid_gcd(e, phi)

    if d != 1:
        e = generate_public_exponent(phi)

    return e


def generate_private_exponent(public_exponent, phi):
    return euclid_extended_gcd(public_exponent, phi)[0]


def generate_keys(p, q):
    if p == q:
        raise ValueError('p and q should not be equal')

    if (p - 1) * (q - 1) < 1024:
        raise ValueError("(p-1)*(q-1) should be greater 1024")

    if not (is_prime(p) and is_prime(q)):
        raise ValueError('p and q should be prime')

    n = p * q
    phi = (p - 1) * (q - 1)

    e = generate_public_exponent(phi)
    d = generate_private_exponent(e, phi)

    while 0 > d != e:
        e = generate_public_exponent(phi)
        d = generate_private_exponent(e, phi)

    return (e, n), (d, n)


def encrypt(message_as_numbers, public_key):
    key, n = public_key

    encrypted_message = [pow(bite, key, n) for bite in message_as_numbers]

    return encrypted_message


def decrypt(message_as_numbers, private_key):
    key, n = private_key

    decrypted_message = [pow(bite, key, n) for bite in message_as_numbers]

    return decrypted_message
