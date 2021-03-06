from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
import base64

# 数据加密
message = "This is a plain text."
with open('rsa.pub', 'r') as f:
    public_key = f.read()
    print(public_key.encode(encoding="utf-8"))
    rsa_key_obj = RSA.importKey(public_key)
    cipher_obj = Cipher_PKCS1_v1_5.new(rsa_key_obj)
    cipher_text = base64.b64encode(cipher_obj.encrypt(message))
    print('cipher test: ', cipher_text)

# 数据解密
with open('rsa.key', 'r') as f:
    private_key = f.read()
    print(private_key.encode(encoding="utf-8"))
    rsa_key_obj = RSA.importKey(private_key)
    cipher_obj = Cipher_PKCS1_v1_5.new(rsa_key_obj)
    random_generator = Random.new().read
    plain_text = cipher_obj.decrypt(base64.b64decode(cipher_text), random_generator)
    print('plain text: ', plain_text)