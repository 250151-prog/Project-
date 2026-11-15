def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def main():
    print("Simple Calculator")
    print("5 + 3 =", add(5, 3))
    print("10 - 4 =", subtract(10, 4))
    print("10 / 2 =", divide(10, 2))
    print("10 / 0 =", divide(10, 0))

if __name__ == "__main__":
    main()
