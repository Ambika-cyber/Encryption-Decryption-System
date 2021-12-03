
from Crypto.Cipher import AES
import binascii, os

def generate_key():
    print("hii key")
    secretKey = os.urandom(32)  # 256-bit random encryption key
    key = binascii.hexlify(secretKey)
    print(key)
    print(key.decode("utf-8"))
    print("hii".encode("utf-8"))
    

generate_key()

secretKey = "3aaeadf4889dea2b0f91c560782d30881c09a3ebf1285bb7ad274c19c014b7e1"
key = secretKey.encode("utf-8")
print("key:",key)
key2 = binascii.unhexlify(key)
print("key2:",key2)

# b":\xae\xad\xf4\x88\x9d\xea+\x0f\x91\xc5`x-0\x88\x1c\t\xa3\xeb\xf1([\xb7\xad'L\x19\xc0\x14\xb7\xe1"
# b":\xae\xad\xf4\x88\x9d\xea+\x0f\x91\xc5`x-0\x88\x1c\t\xa3\xeb\xf1([\xb7\xad'L\x19\xc0\x14\xb7\xe1"