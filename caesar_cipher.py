
def encrypt_text(message, shift):
    encrypted = ""

    for letter in message:
        if letter.isupper():
            new_pos = (ord(letter) - ord('A') + shift) % 26
            encrypted += chr(new_pos + ord('A'))
        elif letter.islower():
            new_pos = (ord(letter) - ord('a') + shift) % 26
            encrypted += chr(new_pos + ord('a'))
        else:
            encrypted += letter

    return encrypted


def decrypt_text(message, shift):
    # decryption is just encryption with the opposite shift
    return encrypt_text(message, -shift)


def main():
    print("=== Caesar Cipher Tool ===")
    user_text = input("Enter the text you want to encrypt: ")

    try:
        key = int(input("Enter a shift value (e.g. 3): "))
    except ValueError:
        print("Please enter a valid number next time.")
        return

    encrypted_msg = encrypt_text(user_text, key)
    decrypted_msg = decrypt_text(encrypted_msg, key)

    print("\nOriginal Text :", user_text)
    print("Encrypted Text:", encrypted_msg)
    print("Decrypted Text:", decrypted_msg)


if __name__ == "__main__":
    main()