import encryption
import algorithms
import string


def main():
    while True:
        print()
        print("(1) Rail Fence encryption")
        print("(2) Key phrase encryption")
        print("(3) Caesar encryption")
        print("(4) Improved Caesar encryption")
        print("(5) Grill rotation encryption")
        print("(0) Exit")

        switch(input(">>>"))


def rail_fence_invoker():
    print()
    print("Rail Fence encryption")

    print("Enter text")
    text = input(">>>")

    print("Enter key")
    key = int(input(">>>"))

    period = (key - 1) * 2
    encrypted_text, fence = encryption.encrypt_rail_fence(text, key)
    decrypted_text = encryption.decrypt_rail_fence(encrypted_text, key)

    for i in range(key):
        for j in range(len(fence[i])):
            if fence[i][j] is None:
                fence[i][j] = " "
        print("".join(fence[i]))

    print("Key:           ", key)
    print("Period:        ", period)
    print("Encrypted text:", encrypted_text)
    print("Decrypted text:", decrypted_text)


def key_phrase_invoker():
    print()
    print("Key phrase encryption")

    print("Enter text")
    text = input(">>>")

    print("Enter key")
    key = input(">>>")

    encrypted_text, indexes, table = encryption.encrypt_key_phrase(text, key)
    decrypted_text = encryption.decrypt_key_phrase(encrypted_text, key)

    for it in key:
        print("%3s" % it, end=" ")
    print()
    for it in indexes:
        print("%3s" % it, end=" ")
    print()
    for it in table:
        for letter in it:
            print("%3s" % letter, end=" ")
        print()
    print()
    print("Encrypted text:", encrypted_text)
    print("Decrypted text:", decrypted_text)


def caesar_invoker():
    alphabet = string.printable

    print()
    print("Caesar encryption")

    print("Enter text")
    text = input(">>>")

    print("Enter key")
    key = int(input(">>>"))

    encrypted_text = encryption.encrypt_caesar(text, key, alphabet)
    decrypted_text = encryption.decrypt_caesar(encrypted_text, key, alphabet)

    print("Encrypted text", encrypted_text)
    print("Decrypted text", decrypted_text)


def improved_caesar_invoker():
    alphabet = string.printable

    print()
    print("Caesar encryption")

    print("Enter text")
    text = input(">>>")

    while True:
        print("Enter key")
        key = int(input(">>>"))

        if algorithms.is_coprime(key, len(alphabet)):
            break

        print("n and key should be coprime")
        print("n =", len(alphabet))

    encrypted_text = encryption.encrypt_improved_caesar(text, key, alphabet)
    decrypted_text = encryption.decrypt_improved_caesar(encrypted_text, key, alphabet)

    print("Encrypted text", encrypted_text)
    print("Decrypted text", decrypted_text)


def grill_rotation_invoker():
    print()
    print("Grill rotation encryption")

    print("Enter text")
    text = input(">>>")

    while True:
        print("Enter n")
        n = int(input(">>>"))

        if n ** 2 > len(text) ** 0.5:
            break

        print("n should be greater then len(text) ** 0.5")

    matrix = encryption.create_matrix(n)
    grid = encryption.create_grid(matrix)
    sieve = encryption.create_sieve(grid)
    encrypted_text, encrypted_table = encryption.encrypt_grid_rotation(text, sieve)
    decrypted_text = encryption.decrypt_grid_rotation(encrypted_text, sieve).strip()

    for it in grid:
        for num in it:
            print("%3s" % num, end=" ")
        print()
    print()
    for it in sieve:
        for boolean in it:
            print("%6s" % boolean, end=" ")
        print()
    print()
    for it in encrypted_table:
        for num in it:
            print("%3s" % num, end=" ")
        print()

    print("Encrypted text:", encrypted_text)
    print("Decrypted text:", decrypted_text)


def switch(case):
    switcher = {
        "1": rail_fence_invoker,
        "2": key_phrase_invoker,
        "3": caesar_invoker,
        "4": improved_caesar_invoker,
        "5": grill_rotation_invoker,
        "0": lambda: exit(0)
    }

    func = switcher.get(case, lambda: "Invalid case")
    return func()


if __name__ == "__main__":
    main()