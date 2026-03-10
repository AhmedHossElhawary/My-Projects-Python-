import string
import random
print("Let's create a strong password for you")
while True:
    while True:
        length = input("Enter the total number of characters for the password: ")
        while not length.isdigit() or length == int(length):
            length = input("Please enter a valid number for the length of the password: ")
        let = input("Enter the number of letters you want in your password: ")
        while not let.isdigit() or let == int(let):
            let = input("Please enter a valid number for the number of letters: ")
        dig = input("Enter the number of digits you want in your password: ")
        while not dig.isdigit() or dig == int(dig):
            dig = input("Please enter a valid number for the number of digits: ")
        sym = input("Enter the number of symbols you want in your password: ")
        while not sym.isdigit() or sym == int(sym):
            sym = input("Please enter a valid number for the number of symbols: ")
        if int(let) + int(dig) + int(sym) != int(length):
            print("The total number of characters does not match the sum of letters, digits, and symbols. Please try again.")
        else:
            break
    def generate():
        password = []
        password.extend(random.choices(string.ascii_letters, k=int(let)))
        password.extend(random.choices(string.digits, k=int(dig)))
        password.extend(random.choices(string.punctuation, k=int(sym)))
        random.shuffle(password)
        print("Your strong password is: " , "".join(password))
    generate()
    chos1 = input("Do you want to generate another password? (yes/no): ")
    while chos1 not in ["yes", "y", "no", "n"]:
        chos1 = input("Please enter 'yes' or 'no': ")
    if chos1 == "no" or chos1 == "n":
        print("Thank you for using the password generator. Goodbye!")
        exit()
    else:
        chos2 = input("Do you want to generate the same structure of the password? (yes/no): ")
        while chos2 not in ["yes", "y", "no", "n"]:
            chos2 = input("Please enter 'yes' or 'no': ")
    if chos2 == "no" or chos2 == "n":
        continue
    while chos2 == "yes" or chos2 == "y":
        generate()
        chos2 = input("Do you want to generate another password? (yes/no): ")
        if chos2 == "no" or chos2 == "n":
            print("Thank you for using the password generator. Goodbye!")
            exit()
    