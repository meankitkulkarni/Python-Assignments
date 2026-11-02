
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