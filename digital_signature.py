import algorithms


def create_signature(message_as_numbers, private_key) -> int:
    key, n = private_key

    hash = algorithms.hash(message_as_numbers, n)
    return algorithms.fast_exponent(hash, key, n)


def check_signature(message_with_sign, public_key):
    key, n = public_key
    message_as_numbers, signature = message_with_sign
    hash1 = algorithms.fast_exponent(signature, key, n)
    hash2 = algorithms.hash(message_as_numbers, n)

    return hash1 == hash2, hash1, hash2
