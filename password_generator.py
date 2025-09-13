import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""
    if use_letters:
        characters += string.ascii_letters   
    if use_numbers:
        characters += string.digits          
    if use_symbols:
        characters += string.punctuation     

    if not characters:
        return "Error: No character sets selected!"

    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")

    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Password length must be a positive number.")
            return
    except ValueError:
        print("Invalid input! Please enter a number.")
        return
    choice = input("Include letters? (y/n): ").lower()
    if choice == "y":
        use_letters = True
    else:
        use_letters = False
    
    choice = input("Include numbers? (y/n): ").lower()
    if choice == "y":
        use_numbers = True
    else:
        use_numbers = False

    choice = input("Include symbol? (y/n): ").lower()
    if choice == "y":
        use_symbols = True
    else:
        use_symbols = False

    password = generate_password(length, use_letters, use_numbers, use_symbols)
    print(f"\n Generated Password: {password}")

if __name__ =="__main__":
    main()        