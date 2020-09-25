from unittest import TestCase
from intermediate.excercises.encryption.crypto import RSACrypto
import os


class TestRSACrypto(TestCase):
    def test_generate_rsa_key(self):
        crypto = RSACrypto()
        key_file = "bob_secret_key_file.pem"
        crypto.generate_rsa_key("I guess so!", key_file=key_file, key_bit_size=4096)

        # Simple test for file existence
        self.assertTrue(os.path.isfile(key_file))

    def test_extract_public_key_from_file(self):
        crypto = RSACrypto()
        key_file = "bob_secret_key_file.pem"
        public_key = crypto.extract_public_key_from_file(passphrase="I guess so!", key_file=key_file)

        with open("receiver.pem", "wb") as file_out:
            file_out.write(public_key)
            file_out.close()

    def test_rsa_encrypt(self):
        crypto = RSACrypto()
        data = "I met aliens in UFO. Here is the map.".encode("utf-8")

        crypto.rsa_encrypt_file(data=data, receiver_key_filename="receiver.pem", file_name_out="encrypted_data.bin")

    def test_rsa_decrypt_file(self):
        crypto = RSACrypto()
        crypto.rsa_decrypt_file(encrypted_file_name="encrypted_data.bin", )



