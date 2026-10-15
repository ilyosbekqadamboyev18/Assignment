def factorial(n):
        if n < 0:
            return "Wrong input"
        result = 1
        for i in range(1, n+1):
            result *= i
        return result
n = int(input())
print(factorial(n))
print(size(n))