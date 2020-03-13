from algorithms import *


def main():
    while True:
        print("(1) Euclidean GCD")
        print("(2) Binary GCD")
        print("(3) Euler function")
        print("(4) Euler theorem")
        print("(5) Reciprocal number by module")
        print("(6) Exponentiation by module")
        print("(0) Exit")

        switch(input(">>>"))


def euclidean_gcd_invoker():
    print()
    print("Euclidean GCD")

    m = int(input("m = "))
    n = int(input("n = "))

    print("GCD =", euclid_gcd(m, n))
    input()


def binary_gcd_invoker():
    print()
    print("Binary GCD")

    m = int(input("m = "))
    n = int(input("n = "))

    print("GCD =", binary_gcd(m, n))
    input()


def euler_function_invoker():
    print()
    print("Euler function")
    print("f(n) = quantity of natural numbers less than n and mutually simple with n")

    n = int(input("n = "))

    print("f(n) =", euler_function(n))
    input()


def euler_theorem_invoker():
    print()
    print("Euler theorem")
    print("a^f(n) = 1 (mod n)")

    a = int(input("a = "))
    n = int(input("n = "))

    if euclid_gcd(a, n) != 1:
        print("a and n are not coprime")
        print()
        return

    print("a^f(n) mod n = 1 mod n")
    print(a, "^f(", n, ") mod ", n, " = 1 mod ", n, sep="")
    print(a ** euler_function(n) % n, "=", 1 % n)
    input()


def reciprocal_number_invoker():
    print()
    print("Reciprocal number by module")
    print("n = m^(f(r) - 1) mod r")

    r = int(input("r = "))
    m = int(input("m = "))

    print("n = ", m, "^(f(", r, ") - 1) mod ", r, sep="")
    print("n =", reciprocal(m, r))
    input()


def exponentiation_by_module_invoker():
    print()
    print("Exponentiation by module")
    print("e = m^n mod r")

    m = int(input("m = "))
    n = int(input("n = "))
    r = int(input("r = "))
    k = int(input("k = "))

    print("e = ", m, "^", n, " mod ", r, sep="")
    print("e = k")
    print(k, "=", m ** n % r)
    input()


def switch(case):
    switcher = {
        "1": euclidean_gcd_invoker,
        "2": binary_gcd_invoker,
        "3": euler_function_invoker,
        "4": euler_theorem_invoker,
        "5": reciprocal_number_invoker,
        "6": exponentiation_by_module_invoker,
        "0": lambda: exit(0)
    }

    func = switcher.get(case, lambda: "Invalid case")
    return func()


if __name__ == "__main__":
    main()
