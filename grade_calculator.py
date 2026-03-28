def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "Fail"

def main():
    try:
        marks = float(input("Enter your marks: "))
        
        if marks < 0 or marks > 100:
            print("Please enter marks between 0 and 100.")
            return
        
        grade = calculate_grade(marks)
        print(f"Your Grade is: {grade}")
    
    except ValueError:
        print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    main()