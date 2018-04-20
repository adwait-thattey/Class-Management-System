# def encrypt(message):
# 	result = ''
# 	for i in range(0, len(message)):
# 		result = result + chr(ord(message[i]) - 2)
# 	return result

# def decrypt(d_message):
# 	result = ''
#     for i in range(0, len(d_message)):
#     	result = result + chr(ord(d_message[i]) + 2)
# 	return result

 
# x = encrypt("Hi")
# print(x)

# def encrypt(message):
# 	result = ''
# 	for i in range(0,len(message)):
# 		result = result + chr(ord(message[i]) - 2)
# 	return result

# def decrypt(d_message):
# 	result = ''
# 	for i in range(0,len(d_message)):
# 		result = result + chr(ord(d_message[i]) + 2)
# 	return result

# x = encrypt("My name is Brijesh")
# y = decrypt(x)
# print(x)
# print(y)

from Crypto import Random
from Crypto.Cipher import AES
import base64

BLOCK_SIZE=16

def encrypt(message, passphrase):
    # passphrase MUST be 16, 24 or 32 bytes long, how can I do that ?
    IV = Random.new().read(BLOCK_SIZE)
    aes = AES.new(passphrase, AES.MODE_CFB, IV)
    return base64.b64encode(aes.encrypt(message))

def decrypt(encrypted, passphrase):
    IV = Random.new().read(BLOCK_SIZE)
    aes = AES.new(passphrase, AES.MODE_CFB, IV)
    return aes.decrypt(base64.b64decode(encrypted))


x = encrypt('keyz','aaquib')
print(x)