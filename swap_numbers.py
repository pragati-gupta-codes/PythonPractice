# Swap Two Numbers

def main():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        print(f"Before swapping: a = {a}, b = {b}")

        # Swapping
        a, b = b, a

        print(f"After swapping: a = {a}, b = {b}")

    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()