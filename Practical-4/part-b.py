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