import string
def encrypt(word, shift):
    alphabet = string.ascii_lowercase
    encrypted_word = ""
    while True:
        try:
            key = int(shift)
            break
        except ValueError:
            key = input("Invalid key. Please enter a number.\n")
    for letter in word:
        if letter in alphabet or letter in alphabet.upper():
            original_position = alphabet.index(letter.lower())
            new_position = (original_position + key) % len(alphabet)
            encrypted_word += alphabet[new_position] if letter.islower() else alphabet[new_position].upper()
        else:
            encrypted_word += letter
    return encrypted_word
message = input("Enter a Message to encrypt: ")
value = input("Enter the shift value: ")
print("Encrypted message:", encrypt(message, value))
