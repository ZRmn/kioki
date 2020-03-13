def euclid_gcd(a, b):
    return euclid_gcd(b, a % b) if b > 0 else a


def euclid_extended_gcd(a, b):
    if b == 0:
        return 1, 0, a

    y, x, g = euclid_extended_gcd(b, a % b)
    return x, y - (a // b) * x, g


def binary_gcd(a, b):
    k = 1
    while a != 0 and b != 0:
        while a % 2 == 0 and b % 2 == 0:
            a /= 2
            b /= 2
            k *= 2

        while a % 2 == 0:
            a /= 2

        while b % 2 == 0:
            b /= 2

        if a >= b:
            a -= b
        else:
            b -= a

    return int(b * k)


def euler_function(n):
    result = n
    i = 2

    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n /= i

            result -= result / i

        i += 1

    if n > 1:
        result -= result / n

    return int(result)


def reciprocal(n, module):
    return n ** (euler_function(module) - 1) % module


def is_prime(num):
    if num == 2:
        return True

    if num < 2 or num % 2 == 0:
        return False

    for n in range(3, int(num ** 0.5) + 2, 2):
        if num % n == 0:
            return False

    return True


def is_coprime(a, b):
    if a == b:
        return a == 1
    elif a > b:
        return is_coprime(a - b, b)
    else:
        return is_coprime(b - a, a)


def fast_exponent(a, z, n):
    a1 = a
    z1 = z
    x = 1

    while z1 != 0:
        while z1 % 2 == 0:
            z1 = z1 / 2
            a1 = a1 ** 2 % n
        z1 = z1 - 1
        x = x * a1 % n

    return x


def hash(message_as_numbers, n, start=31):
    h = start

    for i in message_as_numbers:
        h = (h + i) ** 2 % n

    return h


def rotate_left_matrix(matrix):
    rotated_matrix = []

    for j in range(len(matrix[0])):
        column = []

        for i in range(len(matrix)):
            column += [matrix[i][j]]

        rotated_matrix.insert(0, column)

    return rotated_matrix


def rotate_matrix(matrix):
    rotated_matrix = []

    for j in range(len(matrix[0])):
        column = []

        for i in range(len(matrix)):
            column += [matrix[i][j]]

        column.reverse()
        rotated_matrix += [column]

    return rotated_matrix


def transpose(matrix):
    rotated_matrix = []

    for j in range(len(matrix[0])):
        column = []

        for i in range(len(matrix)):
            column += [matrix[i][j]]

        rotated_matrix += [column]

    return rotated_matrix
