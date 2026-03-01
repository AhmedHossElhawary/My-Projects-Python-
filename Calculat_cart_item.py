print("******* Welcome to iShop calculator *******")
cart = input("How many items are there in your shopping cart? ")
while True:
    if cart.isdigit() and int(cart) > 0:
        break
    while not cart.isdigit() or int(cart) < 0:
        cart = input("Please enter a valid number: ")
    if int(cart) == 0:
        empty = input("Your shopping cart is empty. Are you sure there are no items in your cart? (yes/no) ").lower()
        while empty not in ["yes", "no", "y", "n"]:
            empty = input("Please enter 'yes' or 'no': ").lower()
        if empty == "yes" or empty == "y":
            print("Thank you for visiting iShop. Have a nice day!"), exit()
        else:            
            cart = input("How many items are there in your shopping cart? ")
items = []
for i in range(int(cart)):
    item_name = input(f"Enter the name of item {i + 1}: ")
    while True:
        item_price = input(f"Enter the price of {item_name}: $")
        try:
            item_price = float(item_price)
            if item_price < 0:
                print("Price cannot be negative. Please enter a valid price.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for the price.")
    items.append((item_name, item_price))
Recite = input("Do you want to know the recite of your items? (yes/no) ").lower()
while Recite not in ["yes", "no" ,"y", "n"]:
    Recite = input("Please enter 'yes' or 'no': ").lower()
if Recite == "yes" or Recite == "y":
    print("\nHere are the items in your shopping cart:")
    for item in items:
        print(f"- {item[0]}: ${item[1]:.2f}")
    print (f"\nTotal cost: ${sum(item[1] for item in items):.2f}")
    print("Thank you for using iShop calculator. Have a nice day!")
else:
    print("Thank you for using iShop calculator. Have a nice day!")