# Lab 4 - Task 1: Goldbach's Conjecture


def is_prime(num):
    # Numbers less than 2 are not prime
    if num < 2:
        return False

    # Check if any number from 2 to num - 1 divides num evenly
    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def find_pairs(n):
    # Find all pairs (p, q) where p + q == n and p <= q
    for p in range(2, n // 2 + 1):
        q = n - p
        if is_prime(p) and is_prime(q):
            print(f"{n} = {p} + {q}")


def main():
    text = input("Enter an even number greater than 2: ")

    # Check that input is a valid integer
    if not text.isdigit():
        print("Error: please enter a valid whole number.")
        return

    n = int(text)

    # Check that n is even and greater than 2
    if n <= 2 or n % 2 != 0:
        print("Error: the number must be even and greater than 2.")
        return

    print(f"Pairs for {n}:")
    find_pairs(n)


if __name__ == "__main__":
    main()