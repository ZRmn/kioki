import algorithms
import random
import copy


def encrypt_rail_fence(text, key):
    rail = [[None for i in range(len(text))] for j in range(key)]

    dir_down = False
    row, col = 0, 0

    for i in range(len(text)):
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down

        rail[row][col] = text[i]
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    result = []

    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] is not None:
                result.append(rail[i][j])

    return "".join(result), rail


def decrypt_rail_fence(text, key):
    rail = [[None for i in range(len(text))] for j in range(key)]

    dir_down = None
    row, col = 0, 0

    for i in range(len(text)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        rail[row][col] = "marker"
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    index = 0

    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] == "marker" and index < len(text):
                rail[i][j] = text[index]
                index += 1

    result = []
    row, col = 0, 0

    for i in range(len(text)):
        if row == 0:
            dir_down = True

        if row == key - 1:
            dir_down = False

        if rail[row][col] != "marker":
            result.append(rail[row][col])
            col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    return "".join(result)


def __get_key_indexes(key):
    key_as_numbers = [ord(char) for char in key]
    indexes = [-1] * len(key_as_numbers)

    max_number = max(key_as_numbers) + 1

    for i in range(len(indexes)):
        index = key_as_numbers.index(min(key_as_numbers))
        key_as_numbers[index] = max_number
        indexes[index] = i

    return indexes


def __split_array(array, n):
    return [array[i:i + n] for i in range(0, len(array), n)]


def encrypt_key_phrase(text, key):
    indexes = __get_key_indexes(key)
    table = __split_array(text, len(key))

    if len(table[-1]) < len(key):
        table[-1] += " " * (len(key) - len(table[-1]))

    encrypted_text = []

    for i in range(len(table)):
        key_indexes_dict = dict(zip(indexes, table[i]))

        for j in range(len(table[i])):
            encrypted_text += key_indexes_dict[j]

    return "".join(encrypted_text), indexes, table


def decrypt_key_phrase(text, key):
    indexes = __get_key_indexes(key)
    table = __split_array(text, len(key))

    decrypted_text = []

    for i in range(len(table)):
        for j in range(len(table[i])):
            decrypted_text += table[i][indexes[j]]

    return "".join(decrypted_text)


def encrypt_caesar(text, key, alphabet):
    encrypted_text = ""

    for char in text:
        encrypted_text += alphabet[(alphabet.index(char) + key) % len(alphabet)]

    return encrypted_text


def decrypt_caesar(text, key, alphabet):
    decrypted_text = ""

    for char in text:
        decrypted_text += alphabet[(alphabet.index(char) + len(alphabet) - key) % len(alphabet)]

    return decrypted_text


def encrypt_improved_caesar(text, key, alphabet):
    encrypted_text = ""

    for char in text:
        encrypted_text += alphabet[(alphabet.index(char) * key) % len(alphabet)]

    return encrypted_text


def decrypt_improved_caesar(text, key, alphabet):
    decrypted_text = ""

    for char in text:
        index = (alphabet.index(char) * (algorithms.euclid_extended_gcd(key, len(alphabet))[0])) % len(alphabet)
        decrypted_text += alphabet[index]

    return decrypted_text


def create_matrix(n):
    matrix = [[-1] * n for i in range(n)]

    cell_value = 1

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = cell_value
            cell_value += 1

    return matrix


def create_grid(matrix):
    grid = [[-1] * len(matrix) * 2 for i in range(len(matrix) * 2)]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            grid[i][j] = matrix[i][j]

    rotated_matrix = algorithms.rotate_matrix(matrix)

    for i in range(len(rotated_matrix)):
        for j in range(len(rotated_matrix[i])):
            grid[i][j + len(rotated_matrix)] = rotated_matrix[i][j]

    rotated_matrix = algorithms.rotate_matrix(rotated_matrix)

    for i in range(len(rotated_matrix)):
        for j in range(len(rotated_matrix[i])):
            grid[i + len(rotated_matrix)][j + len(rotated_matrix)] = rotated_matrix[i][j]

    rotated_matrix = algorithms.rotate_matrix(rotated_matrix)

    for i in range(len(rotated_matrix)):
        for j in range(len(rotated_matrix[i])):
            grid[i + len(rotated_matrix)][j] = rotated_matrix[i][j]

    return grid


def create_sieve(grid):
    sieve = [[False] * len(grid) for i in range(len(grid))]

    for i in range(1, int(len(grid) / 2) ** 2 + 1):
        while True:
            index = random.randrange(0, len(grid))

            if i in grid[index]:
                sieve[index][grid[index].index(i)] = True
                break

    return sieve


def get_sieve_indexes(sieve):
    indexes = []

    for i in range(len(sieve)):
        for j in range(len(sieve[i])):
            if sieve[i][j]:
                indexes.append((i, j))

    return indexes


def encrypt_grid_rotation(text, sieve):
    sieve_copy = copy.deepcopy(sieve)

    holes = int(len(sieve_copy) / 2) ** 2
    splitted_text = __split_array(text, holes)
    encrypted_table = [[" "] * len(sieve_copy) for i in range(len(sieve_copy))]

    for i in range(len(splitted_text)):
        sieve_indexes = get_sieve_indexes(sieve_copy)

        for j in range(len(splitted_text[i])):
            sieve_i, sieve_j = sieve_indexes[j]
            encrypted_table[sieve_i][sieve_j] = splitted_text[i][j]

        sieve_copy = algorithms.rotate_matrix(sieve_copy)

    encrypted_text = ""

    for it in encrypted_table:
        encrypted_text += "".join(it)

    return encrypted_text, encrypted_table


def decrypt_grid_rotation(text, sieve):
    sieve_copy = copy.deepcopy(sieve)
    holes = int(len(sieve_copy) / 2) ** 2
    splitted_text = __split_array(text, holes)
    encrypted_table = __split_array(text, len(sieve_copy))
    decrypted_text = ""

    for i in range(len(splitted_text)):
        sieve_indexes = get_sieve_indexes(sieve_copy)

        for j in range(len(splitted_text[i])):
            sieve_i, sieve_j = sieve_indexes[j]
            decrypted_text += encrypted_table[sieve_i][sieve_j]

        sieve_copy = algorithms.rotate_matrix(sieve_copy)

    return decrypted_text
