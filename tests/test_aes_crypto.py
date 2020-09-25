from unittest import TestCase
import os
from Crypto.Protocol.KDF import PBKDF2
from intermediate.excercises.encryption.aes_crypto import AESCrypto

class TestAESCrypto(TestCase):
    def setUp(self) -> None:
        self.xfiles = "xfiles.bin"
        self.aes_key_file = "secret_to_xfiles.bin"
        self.aes_key = None
        self.salt = b'J\xf6\x1eP<yT\x08\xf8\xa2\x80K\xe9\xfaB=\xa8\x1fzxp$\xee\xf7\xa6\xd9\x9d\x9cd\xf2\xe7\x15'
        self.test_password = b'I could not guess that'

    def test_generate_random_key(self):
        aes_crypto = AESCrypto()
        self.aes_key = aes_crypto.generate_random_key(self.aes_key_file)

    def test_encrypt(self):
        key = PBKDF2(self.test_password, self.salt, dkLen=32)  # Your key that you can encrypt with

        aes_crypto = AESCrypto()
        aes_crypto.encrypt(b'The space aliens took me up to their ship and probed me!', key, self.xfiles)

        # This is should not be considered enough for production code.
        self.assertTrue(os.path.isfile("xfiles.bin"))

    def test_decrypt(self,):

        key = PBKDF2(self.test_password, self.salt, dkLen=32)  # Your key that you can encrypt with
        aes_crypto = AESCrypto()

        original_data = aes_crypto.decrypt(self.xfiles, key, self.salt)
        print(original_data)

    def tearDown(self) -> None:
        pass
        # if os.path.isfile(self.xfiles):
        #     os.remove(self.xfiles)

    def test_generate_salt(self):
        aes_crypto = AESCrypto()
        aes_crypto.generate_salt()
