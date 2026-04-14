# Reverse a Number

def reverse_number(n):
    return int(str(n)[::-1])

def main():
    try:
        num = int(input("Enter a number: "))
        print("Reversed number:", reverse_number(num))
    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()