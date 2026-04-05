# Factorial Program

def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    try:
        num = int(input("Enter a number to find factorial: "))
        print("Factorial:", factorial(num))
    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()