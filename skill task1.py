def caesar_cipher(message, shift):
    """Encrypt or decrypt a message using the Caesar cipher algorithm."""
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            # Determine the starting ASCII code for uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around using modulo operation
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            encrypted_message += shifted_char
        else:
            # Non-alphabet characters remain unchanged
            encrypted_message += char
    return encrypted_message

def main():
    print("Welcome to the Caesar Cipher Program!")

    # Get user choice
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()

    if choice not in ['E', 'D']:
        print("Invalid choice. Please enter 'E' to encrypt or 'D' to decrypt.")
        return

    # Get the message from the user
    message = input("Enter your message: ")

    # Get the shift value from the user
    try:
        shift = int(input("Enter the shift value (an integer): "))
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        return

    # Adjust shift value for decryption
    if choice == 'D':
        shift = -shift

    # Encrypt or decrypt the message
    result = caesar_cipher(message, shift)

    # Output the result
    if choice == 'E':
        print(f"Encrypted message: {result}")
    else:
        print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()


