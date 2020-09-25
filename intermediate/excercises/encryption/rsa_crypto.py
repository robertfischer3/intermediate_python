from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

class AESCrypto:
    def encrypt(self, data, file_to_encrypt):
        key = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(data)

        with open(file_to_encrypt, "wb") as file_out:
            [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]

    def decrypt(self, file_to_decrypt, key):
         with open(file_to_decrypt, "rb") as file_in:
            nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)]

            # let's assume that the key is somehow available again
            cipher = AES.new(key, AES.MODE_EAX, nonce)
            data = cipher.decrypt_and_verify(ciphertext, tag)
            return data

class RSACrypto:

    def generate_rsa_key(self, passphrase, key_file="rsa_key.bin", key_bit_size=2048):
        key = RSA.generate(key_bit_size)
        encrypted_key = key.export_key(passphrase=passphrase, pkcs=8,
                                       protection="scryptAndAES128-CBC")

        with open(key_file, "wb") as file_out:
            file_out.write(encrypted_key)
            file_out.close()

    def extract_public_key_from_file(self, passphrase, key_file="rsa_key.bin"):

        with open(key_file, "rb") as encrypted_key:
            encoded_key = encrypted_key.read()
        key = RSA.import_key(encoded_key, passphrase=passphrase)

        print(key.publickey().export_key())
        return key.publickey().export_key()

    def rsa_encrypt_file(self, data, receiver_key_filename, file_name_out):

        with open(receiver_key_filename) as  receiver_key:
            recipient_key = RSA.import_key(receiver_key.read())
            if receiver_key is None:
                raise
            with open(file_name_out, "wb") as file_out:
                session_key = get_random_bytes(16)

                # Encrypt the session key with the public RSA key
                cipher_rsa = PKCS1_OAEP.new(recipient_key)
                enc_session_key = cipher_rsa.encrypt(session_key)

                # Encrypt the data with the AES session key
                cipher_aes = AES.new(session_key, AES.MODE_EAX)
                ciphertext, tag = cipher_aes.encrypt_and_digest(data)
                [file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext)]
                file_out.close()

    def rsa_decrypt_file(self, encrypted_file_name, private_key_file):

        with open(encrypted_file_name, "rb") as file_in:
            with open(private_key_file) as private_key:
                private_key = RSA.import_key(private_key.read())

            enc_session_key, nonce, tag, ciphertext = \
                [file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)]

            # Decrypt the session key with the private RSA key
            cipher_rsa = PKCS1_OAEP.new(private_key)
            session_key = cipher_rsa.decrypt(enc_session_key)

            # Decrypt the data with the AES session key
            cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
            data = cipher_aes.decrypt_and_verify(ciphertext, tag)
            print(data.decode("utf-8"))

            return data.decode("utf-8")