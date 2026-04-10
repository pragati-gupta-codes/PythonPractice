# Multiplication Table

def table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

def main():
    try:
        num = int(input("Enter a number: "))
        table(num)
    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()