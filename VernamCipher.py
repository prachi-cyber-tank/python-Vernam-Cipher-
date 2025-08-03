def vernam_cipher_encrypt(plaintext, key):
  
    # Ensure the key and plaintext are of the same length
    if len(plaintext) != len(key):
        print("Error: Plaintext and key must be of the same length for Vernam cipher.")
        return

    print(f"Encrypting '{plaintext}' with key '{key}' using Vernam Cipher.\n")
    print("-" * 60)
    print(f"{'Char':<8} | {'Plaintext (ASCII)':<20} | {'Key (ASCII)':<15} | {'XOR Result (Decimal)':<22} | {'XOR Result (Binary)'}")
    print("-" * 60)

    # This list will store the final encrypted characters
    encrypted_chars = []

    # Process each character
    for i in range(len(plaintext)):
        plain_char = plaintext[i]
        key_char = key[i]

        # 1. Convert each character to its ASCII value
        plain_ascii = ord(plain_char)
        key_ascii = ord(key_char)

        # 2. Perform bitwise XOR on corresponding characters
        xor_result_decimal = plain_ascii ^ key_ascii

        # Convert the decimal XOR result to a binary string for display
        # The format '08b' ensures it's padded with leading zeros to be 8 bits long
        xor_result_binary = format(xor_result_decimal, '08b')
        
        # Store the resulting character of the encryption
        encrypted_chars.append(chr(xor_result_decimal))

        # 3. & 4. Display the values in a formatted table
        print(f"{plain_char:<8} | {plain_ascii:<20} | {key_ascii:<15} | {xor_result_decimal:<22} | {xor_result_binary}")

    # Combine the resulting characters to form the final ciphertext
    ciphertext = "".join(encrypted_chars)
    
    print("-" * 60)
    print(f"\nFinal Ciphertext (as characters): {ciphertext}")
    print(f"Final Ciphertext (as decimal ASCII values): {[ord(c) for c in ciphertext]}")


# --- Main Execution ---
plaintext_word = "CAT"
key_word = "DOG"
vernam_cipher_encrypt(plaintext_word, key_word)
