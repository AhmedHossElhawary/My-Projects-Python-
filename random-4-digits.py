import random
rand = random.randint(0000, 9999)
chos = f"{rand:04d}"
ans = input("""The computer will generate a random 4-digit number.
Enter a 4-digit number: """)
if chos == ans:
    print("""Congratulations! you answer is the same as the computer's number is {}""".format(chos))
elif len(str(ans)) < 4 and ans.isdigit():
    print("Your answer is less than 4-digit number.")
elif len(str(ans)) > 4 and ans.isdigit():
    print("Your answer is more than 4-digit number.")
elif ans != chos and ans.isdigit():
    print("""Sorry, you answer is different from the computer's number.
The computer's number is {}""".format(chos))
else:
    print("Invalid answer.")