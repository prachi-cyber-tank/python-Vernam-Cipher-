Vernam Cipher (One-Time Pad)

This document provides an explanation for a Python script that demonstrates the Vernam Cipher, a method of encryption that uses a one-time pad. This project is intended for educational purposes to illustrate the principles of a theoretically unbreakable cipher.

What is a Vernam Cipher?

The Vernam Cipher, also known as a one-time pad, is an encryption technique that cannot be cracked if used correctly. Its security relies on a few strict rules:

The key must be truly random.

The key must be at least as long as the plaintext message.

The key must never be reused in whole or in part.

The core of the cipher is the combination of the plaintext with the key using a bitwise XOR operation.

How it works:

Each character in the plaintext is converted to its numerical representation (like an ASCII value). The same is done for the corresponding character in the key. These two numerical values are then combined using XOR. The resulting number is converted back into a character, forming the ciphertext.

The Magic of XOR: Encryption and Decryption
The beauty of the Vernam cipher lies in the properties of the XOR operation. XOR is its own inverse. This means:

(Plaintext XOR Key) = Ciphertext

And, therefore:

(Ciphertext XOR Key) = Plaintext

This is why the same process can be used for both encrypting and decrypting a message. Our script focuses on encryption, but to decrypt the output, you would simply run the same XOR process on the ciphertext using the identical key.

Code Breakdown
The provided script demonstrates the encryption process with a detailed, step-by-step output.

vernam_cipher_encrypt(plaintext, key)
This is the main function that performs the encryption.

def vernam_cipher_encrypt(plaintext, key):
    # Ensure the key and plaintext are of the same length
    if len(plaintext) != len(key):
        raise ValueError("Plaintext and key must be of the same length.")

    encrypted_chars = []
    for i in range(len(plaintext)):
        # Convert characters to ASCII values
        plain_ascii = ord(plaintext[i])
        key_ascii = ord(key[i])

        # Perform bitwise XOR and convert back to a character
        xor_result_char = chr(plain_ascii ^ key_ascii)
        encrypted_chars.append(xor_result_char)

    # Join the characters to form the final ciphertext
    return "".join(encrypted_chars)

Length Check: The function first checks if the plaintext and key are the same length, which is a requirement for this implementation of the Vernam cipher.

Character Processing Loop:

It iterates through the plaintext and key, character by character.

ord(): Converts the plaintext and key characters into their respective ASCII integer values.

^: The bitwise XOR operator is applied to the two ASCII values.

chr(): The resulting integer from the XOR operation is converted back into a character.

Final Ciphertext: The list of encrypted characters is joined into a single string and returned.

Main Execution
This section sets the plaintext and key values and calls the main encryption function to begin the process.
