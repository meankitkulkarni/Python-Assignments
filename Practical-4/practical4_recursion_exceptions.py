def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print("Factorial of 4:", factorial(4))

def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))

def recursive_search(items, target, index=0):
    if index >= len(items):
        return -1

    if items[index] == target:
        return index

    return recursive_search(items, target, index + 1)


print(recursive_search([8, 3, 12, 7], 12))
print(recursive_search([8, 3, 12, 7], 5))

print(factorial(0))
print(factorial(1))
print(factorial(5))

print(recursive_search([8, 3, 12], 8))
print(recursive_search([8, 3, 12], 12))
print(recursive_search([8, 3, 12], 5))


def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


# Custom exception class
class InvalidInputError(Exception):
    """Raised when user input violates the application's rules."""


# Function to read and validate user input
def read_non_negative_integer():
    raw = input("Enter a non-negative integer: ")

    try:
        value = int(raw)

        if value < 0:
            raise InvalidInputError("Number cannot be negative.")

    except ValueError:
        print("Input error: enter a whole number, such as 4.")
        return None

    except InvalidInputError as error:
        print(f"Validation error: {error}")
        return None

    else:
        print("Input accepted.")
        return value

    finally:
        print("Input validation attempt finished.")


# Main program
number = read_non_negative_integer()

if number is not None:
    print("Factorial:", factorial(number))


def factorial_buggy(n):
    if n == 0:
        return 0

    return n * factorial_buggy(n - 1)

print("Buggy factorial(4):", factorial_buggy(4))

def factorial_fixed(n):
    if n == 0:
        return 1

    return n * factorial_fixed(n - 1)

print("Fixed factorial(0):", factorial_fixed(0))
print("Fixed factorial(4):", factorial_fixed(4))

# Debugging Note:
# The buggy factorial function returned 0 instead of 24.
# I set a breakpoint inside factorial_buggy and inspected n
# as the recursive calls reached the base case.
# I found that the base case incorrectly returned 0.
# I changed the return value to 1 and verified the result.