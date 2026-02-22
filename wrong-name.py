me = input("Who is the most handsome man in the world? \n")
while True:
    if me.lower() == "ahmed" or me.lower() == "ahmed hossam" or me.lower() == "hossam" or me.lower() == "hossam hassan" or me.lower() == "ahmed hossam hassan" or me.lower() == "you":
        print("Habibi")
        break
    elif me.lower() == "the prophet mohammed" or me.lower() == "prophet mohammed" or me.lower() == "pbuh":
        print("Respect")
        break
    else:
        me = input("You are wrong :(. Try again: \n")