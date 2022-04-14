def multiply(a, b):
    result = a * b
    result2 = a ** b
    return result, result2


print(multiply(5, 6))
b = multiply(2, 3)
print(b)

print(multiply(2, 4)[1])
