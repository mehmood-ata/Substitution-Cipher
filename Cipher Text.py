
import random
import string
import json
import os

CHARS = list(" " + string.punctuation + string.digits + string.ascii_letters)
KEY_FILE = "cipher_key.json"


def load_or_create_key():
    """Load an existing shuffled key from disk, or create and save a new one."""
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "r") as f:
            key = json.load(f)
        print(f"(Loaded existing key from {KEY_FILE})")
    else:
        key = CHARS.copy()
        random.shuffle(key)
        with open(KEY_FILE, "w") as f:
            json.dump(key, f)
        print(f"(Generated new key and saved to {KEY_FILE})")
    return key


def encrypt(text, chars, key):
    char_to_index = {c: i for i, c in enumerate(chars)}
    result = []
    for letter in text:
        if letter not in char_to_index:
            print(f"Warning: skipping unsupported character {letter!r}")
            continue
        result.append(key[char_to_index[letter]])
    return "".join(result)


def decrypt(text, chars, key):
    key_to_index = {c: i for i, c in enumerate(key)}
    result = []
    for letter in text:
        if letter not in key_to_index:
            print(f"Warning: skipping unsupported character {letter!r}")
            continue
        result.append(chars[key_to_index[letter]])
    return "".join(result)


def main():
    key = load_or_create_key()

    while True:
        choice = input("Encrypt or decrypt? (e/d, or q to quit): ").strip().lower()

        if choice == "e":
            plain_text = input("Enter a message to encrypt: ")
            cipher_text = encrypt(plain_text, CHARS, key)
            print(f"original message : {plain_text}")
            print(f"encrypted message: {cipher_text}")

        elif choice == "d":
            cipher_text = input("Enter a message to decrypt: ")
            plain_text = decrypt(cipher_text, CHARS, key)
            print(f"encrypted message: {cipher_text}")
            print(f"original message : {plain_text}")

        elif choice == "q":
            print("Goodbye!")
            break

        else:
            print("Please enter 'e' for encrypt, 'd' for decrypt, or 'q' to quit.")

        print()  # blank line for readability between rounds


if __name__ == "__main__":
    main()