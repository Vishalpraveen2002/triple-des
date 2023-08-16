import pyDes
import os
from bitstring import BitArray

# Function to generate a random key
def generate_key():
    # Generate 24 random bytes
    key = os.urandom(24)
    return key


# Function to encrypt using triple DES
def triple_des_encrypt(key, plaintext):
    # Create the triple DES object
    des3 = pyDes.triple_des(key, pyDes.ECB, padmode=pyDes.PAD_PKCS5)

    # Encrypt the plaintext
    ciphertext = des3.encrypt(plaintext)

    # Return the encrypted ciphertext
    return ciphertext


# Function to decrypt using triple DES
def triple_des_decrypt(key, ciphertext):
    # Create the triple DES object
    des3 = pyDes.triple_des(key, pyDes.ECB, padmode=pyDes.PAD_PKCS5)

    # Decrypt the ciphertext
    plaintext = des3.decrypt(ciphertext)

    # Return the decrypted plaintext
    return plaintext


# Main program
if __name__ == '__main__':
    # Generate a random encryption key

    key = generate_key()

    # Define the plaintext
    plaintext = 'Hello'
    bit_string = ''.join(format(byte, '08b') for byte in bytes(plaintext.encode()))
    print(bit_string)
    print(len(bit_string))
    # Encrypt the plaintext using triple DES
    ciphertext = triple_des_encrypt(key, plaintext.encode())
    print('Ciphertext:', ciphertext)


    bit_string = ''.join(format(byte, '08b') for byte in ciphertext)
    print(bit_string)
    print(len(bit_string))

    # Decrypt the ciphertext using triple DES
    decrypted_text = triple_des_decrypt(key, ciphertext)
    print('Decrypted Text:', decrypted_text.decode())

    bit_string = ''.join(format(byte, '08b') for byte in bytes(decrypted_text))

    print(bit_string)
    print(len(bit_string))