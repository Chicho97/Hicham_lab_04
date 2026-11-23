# Lab 4 - Task 2: Addition and Multiplication of Large Numbers (up to 200 digits)


def clean_zeros(num_str):
    # Remove extra leading zeros, e.g. "00999" -> "999", keep "0" if all zeros
    cleaned = num_str.lstrip("0")
    return cleaned if cleaned != "" else "0"


def is_valid_number(num_str):
    # Must be digits only and at most 200 digits long
    if not isinstance(num_str, str):
        return False
    if len(num_str) == 0 or len(num_str) > 200:
        return False
    return num_str.isdigit()


def validate_number(num_str):
    # Validate and return cleaned number string; raise ValueError if invalid
    if not isinstance(num_str, str) or len(num_str) == 0 or len(num_str) > 200 or not num_str.isdigit():
        raise ValueError("Invalid number: must be 1 to 200 digits.")
    return clean_zeros(num_str)


def add_big_numbers(a, b):
    # Add two number strings from right to left like on paper
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry > 0:
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0

        total = digit_a + digit_b + carry
        result.append(str(total % 10))  # current digit
        carry = total // 10              # carry for next step

        i -= 1
        j -= 1

    # Reverse because we added from right to left
    result.reverse()
    return clean_zeros("".join(result))


def add_numbers(a, b):
    return add_big_numbers(a, b)


def multiply_big_numbers(a, b):
    # Handle 0 and 1 cases cleanly
    if a == "0" or b == "0":
        return "0"
    if b == "1":
        return a
    if a == "1":
        return b

    # Array to store intermediate digit sums
    temp = [0] * (len(a) + len(b))

    # Multiply digit by digit from right to left
    for i in range(len(a) - 1, -1, -1):
        for j in range(len(b) - 1, -1, -1):
            prod = int(a[i]) * int(b[j])
            pos1 = i + j
            pos2 = i + j + 1

            total = prod + temp[pos2]
            temp[pos2] = total % 10
            temp[pos1] += total // 10

    result_str = "".join(str(x) for x in temp)
    return clean_zeros(result_str)


def multiply_numbers(a, b):
    return multiply_big_numbers(a, b)


def main():
    try:
        with open("numere.txt", "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines() if line.strip() != ""]
    except FileNotFoundError:
        print("Error: numere.txt was not found.")
        return

    if len(lines) != 2:
        print("Error: numere.txt must contain two numbers, one per line.")
        return

    try:
        num1 = validate_number(lines[0])
        num2 = validate_number(lines[1])
    except ValueError:
        print("Error: each number must have 1 to 200 digits and contain only digits.")
        return

    print("First number:", num1)
    print("Second number:", num2)
    print("Sum:", add_numbers(num1, num2))
    print("Product:", multiply_numbers(num1, num2))


if __name__ == "__main__":
    main()