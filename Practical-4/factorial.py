def factorial_i(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


def factorial_r(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_r(n - 1)


n = int(input("Enter a number: "))

print("Factorial using iteration =", factorial_i(n))

n = int(input("Enter n: "))

print("Factorial using recursion =", factorial_r(n))
