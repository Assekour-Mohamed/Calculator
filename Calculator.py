c = input("Enter an operation (+, -, *, /): ")

result = None

if c == "+":
    result = m + n
elif c == "-":
    result = m - n
elif c == "*":
    result = m * n
elif c == "/":
    if n != 0:
        result = m / n
    else:
        print("Division by zero is not allowed.")
print(result)
