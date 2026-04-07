# Fibonacci Series

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

def main():
    try:
        num = int(input("Enter number of terms: "))
        fibonacci(num)
    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()