
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
