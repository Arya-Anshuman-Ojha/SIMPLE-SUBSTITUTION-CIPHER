# SIMPLE-SUBSTITUTION-CIPHER
Extremely elementary code for demonstrating how substitution ciphers work.

## Generating the key
The `generate_key.py` script creates two `.dat` files that contain the encryption and decryption keys. Only letters from the English alphabet are substituted, using some random permutation.

## Encryption
After successful key generation, text can be encrypted easily through the terminal in the directory where the keys are stored.
For encrypting text files: `python encrypt.py file <file_name>.txt`. This encrypts the file `<file_name>.txt` and stores the ciphertext in a new file, all in the same directory as the keys.
For simply encrypting text: `python encrypt.py text "<your text here>"`. This simply prints the ciphertext in the terminal itself.

## Decryption
After successful key generation, text can be decrypted easily through the terminal in the directory where the keys are stored.
For decrypting text files: `python decrypt.py file <file_name>.txt`. This decrypts the file `<file_name>.txt` and stores the message in a new file, all in the same directory as the keys.
For simply decrypting text: `python decrypt.py text "<your text here>"`. This simply prints the message in the terminal itself.
