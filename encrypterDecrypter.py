def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Function for brute-force decryption
def brute_force_decrypt(text):
    print("\nTrying all possible shifts (1-25):\n")
    for shift in range(1, 26):
        possible_decryption = decrypt(text, shift)
        print(f"Shift {shift}: {possible_decryption}")

# Main function to run the encrypter/decrypter
def main():
    while True:
        mode = input("Do you want to (e)ncrypt, (d)ecrypt, or (q)uit? ").lower()

        if mode == 'q':
            print("Exiting the program.")
            break

        if mode not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit.")
            continue

        text = input("Enter the text: ")

        if mode == 'e':
            shift = int(input("Enter the shift value (1-25): "))
            result = encrypt(text, shift)
            print(f"Encrypted Text: {result}")
        elif mode == 'd':
            print("Performing brute-force decryption...\n")
            brute_force_decrypt(text)

        # Return to Main Menu
        while True:
            print("\nChoose an option:")
            print("1. Return to Main Menu")
            choice = input("Enter your choice (1): ")

            if choice == '1':
                break
            else:
                print("Invalid choice. Please enter 1.")

if __name__ == "__main__":
    main()