def caesar(text, shift, encrypt=True):
    """
    Encrypts or decrypts a message using the Caesar Cipher.
    
    Args:
        text (str): The message to encrypt/decrypt.
        shift (int): Number of letters to shift (1-25).
        encrypt (bool): True to encrypt, False to decrypt.
    
    Returns:
        str: The encrypted or decrypted message.
    """
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if not encrypt:
        shift = -shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(),
                                      shifted_alphabet + shifted_alphabet.upper())
    return text.translate(translation_table)


def encrypt(text, shift):
    return caesar(text, shift)


def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


# Interactive usage as per README
def main():
    print("Welcome to Caesar Cipher 🔐")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()
    
    if choice not in ['e', 'd']:
        print("Invalid choice! Please enter E or D.")
        return

    text = input("Enter your message: ")
    try:
        shift = int(input("Enter shift (1-25): "))
    except ValueError:
        print("Shift must be an integer!")
        return

    if choice == 'e':
        result = encrypt(text, shift)
        print(f"Encrypted message: {result}")
    else:
        result = decrypt(text, shift)
        print(f"Decrypted message: {result}")


if __name__ == "__main__":
    main()
