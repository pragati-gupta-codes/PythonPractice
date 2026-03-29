def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

def main():
    user_input = input("Enter a word or sentence: ")
    
    if is_palindrome(user_input):
        print("It is a palindrome!")
    else:
        print("Not a palindrome.")

if __name__ == "__main__":
    main()