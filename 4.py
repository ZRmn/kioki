import algorithms
import rsa
import digital_signature


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

        message_as_numbers = numbers_from_letters(message)
        signature = digital_signature.create_signature(message_as_numbers, private_key)
        message_with_sign = message_as_numbers, signature
        is_actual_signature, hash1, hash2 = digital_signature.check_signature(message_with_sign, public_key)

        print("Signature                           :", signature)
        print("Hash from signature and public key  :", hash1)
        print("Hash from message and hash function :", hash2)
        print("Is actual signature                 :", is_actual_signature)

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
