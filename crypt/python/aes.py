import eel
from cryptography.fernet import Fernet
import base64
import logging
import traceback
import pymysql
from Crypto.Cipher import AES
import binascii, os

# def encrypt_AES_GCM(msg, secretKey):
#     aesCipher = AES.new(secretKey, AES.MODE_GCM)
#     ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
#     # return (ciphertext, aesCipher.nonce, authTag)
#     encoded= binascii.hexlify(ciphertext)
#     return encoded

# def decrypt_AES_GCM(encryptedMsg, secretKey):
#     (ciphertext, nonce, authTag) = encryptedMsg
#     aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
#     plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
#     return plaintext

# Key = os.urandom(32)  # 256-bit random encryption key
# print("Encryption key:", binascii.hexlify(secretKey))

# msg = b'Message for AES-256-GCM + Scrypt encryption....jhdg7w##$#$$$jkcdjdgdg54621hv2b dhgfhg hdghg'
# encryptedMsg = encrypt_AES_GCM(msg, secretKey)
# print("encryptedMsg", {
#     'ciphertext': binascii.hexlify(encryptedMsg[0]),
#     'aesIV': binascii.hexlify(encryptedMsg[1]),
#     'authTag': binascii.hexlify(encryptedMsg[2])
# })

# decryptedMsg = decrypt_AES_GCM(encryptedMsg, secretKey)
# print("decryptedMsg", decryptedMsg)

from os import urandom
from Crypto.Cipher import AES

# For Generating cipher text
secret_key = urandom(16)
print(secret_key)
print("Encryption key:", binascii.hexlify(secret_key))
iv = urandom(16)
print("iv",iv)
obj = AES.new(secret_key, AES.MODE_CBC, iv)

# Encrypt the message
message = b'Lorem Ipsum text'
print('Original message is: ', message)
encrypted_text = obj.encrypt(message)
print('The encrypted text', encrypted_text)


# Decrypt the message
rev_obj = AES.new(secret_key, AES.MODE_CBC, iv)
decrypted_text = rev_obj.decrypt(encrypted_text)
print('The decrypted text', decrypted_text.decode('utf-8'))


def AES_encrypt(msg,key):
    print(msg)
    encrypted_text = obj.encrypt(msg)
    encoded= binascii.hexlify(encrypted_text)
    print("encoded:",encoded)
    data2 = encoded.decode("utf-8")
    return encoded


print("key:",secret_key)
print("encr:",encrypted_text)
def AES_decrypt(msg,key):
    
    rev_obj = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = rev_obj.decrypt(encrypted_text)
    print(decrypted_text.decode("utf-8"))


print("function called:")
msg2 = AES_encrypt(message,secret_key)

AES_decrypt(msg2,secret_key)


msg_sq = "hii{{{"

if "{" in msg_sq:
    print("yes")
    msg_sq2 = msg_sq.replace("{","")
    print(msg_sq2)