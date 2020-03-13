import algorithms
import rsa


def main():
    p = 9967
    q = 9973

    print("Use default p and q (y/n)")
    choice = input(">>>")

    if choice == "n":
        p, q = input_p_and_q()

    public_key, private_key = rsa.generate_keys(p, q)
    n = p * q
    phi = (p - 1) * (q - 1)

    while True:
        print()
        print("p           :", p)
        print("q           :", q)
        print("n           :", n)
        print("phi         :", phi)
        print("Public key  :", public_key[0])
        print("Private key :", private_key[0])
        print()
        print("Enter message")

        message = input(">>>")

        if message == "~":
            exit(0)

        encrypted_message = rsa.encrypt(numbers_from_letters(message), public_key)
        decrypted_message = rsa.encrypt(encrypted_message, private_key)

        print("Message                            :", message)
        print("Message as bytes array             :", numbers_from_letters(message))
        print("Encrypted message as numbers array :", encrypted_message)
        print("Decrypted message as numbers array :", decrypted_message)
        print("Decrypted message                  :", "".join(letters_from_numbers(decrypted_message)))

        input()


def letters_from_numbers(numbers):
    return [chr(num) for num in numbers]


def numbers_from_letters(letters):
    return [ord(char) for char in letters]


def input_p_and_q():
    while True:
        p = int(input("p = "))
        q = int(input("q = "))

        if p == q:
            print("p and q should not be equal")
            continue

        if (p - 1) * (q - 1) < 1024:
            print("(p-1)*(q-1) should be greater 1024")
            continue

        if not (algorithms.is_prime(p) and algorithms.is_prime(q)):
            print("p and q should be prime")
            continue

        return p, q


if __name__ == "__main__":
    main()