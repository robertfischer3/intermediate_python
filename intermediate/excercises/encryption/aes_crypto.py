import os

from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import unpad
from Crypto.Util.Padding import pad

class AESCrypto:

    def generate_salt(self):
        salt = get_random_bytes(32)
        print(salt)  # Print the salt to be copied to your script
        return salt

    def generate_random_key(self, key_location, write_to_file=True):
        # Generate the key
        key = get_random_bytes(32)
        # Save the key to a file
        if os.path.isfile(key_location):
            # We never want to overwrite a key file accidently
            raise FileExistsError
        if write_to_file:
            with open(key_location, "wb") as file_out:  # wb = write bytes
                file_out.write(key)
        return key

    def encrypt(self, data, key, encrypt_to_file):

        # encrypt_to_file = 'encrypted.bin'  # Output file
        # data = b'Your data....'  # Must be a bytes object
        # key = b'YOUR KEY'  # The key you generated

        # Create cipher object and encrypt the data
        cipher = AES.new(key, AES.MODE_CBC)  # Create a AES cipher object with the key using the mode CBC
        ciphered_data = cipher.encrypt(pad(data, AES.block_size))  # Pad the input data and then encrypt

        with open(encrypt_to_file, "wb") as file_out:  # Open file to write bytes
            file_out.write(cipher.iv)  # Write the iv to the output file (will be required for decryption)
            file_out.write(
                ciphered_data)  # Write the varying length ciphertext to the file (this is the encrypted data)

    def decrypt(self, file_to_decrypt, password, salt):
        # Read the data from the file
        with open(file_to_decrypt, 'rb') as file_in:  # Open the file to read bytes
            iv = file_in.read(16)  # Read the iv out - this is 16 bytes long
            ciphered_data = file_in.read()  # Read the rest of the data

            cipher = AES.new(password, AES.MODE_CBC, iv=salt)  # Setup cipher
            original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size)  # Decrypt and then up-pad the result
            return original_data
