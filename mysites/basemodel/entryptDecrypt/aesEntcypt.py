from Crypto.Cipher import AES

# 加密与解密所使用的密钥，长度必须是16的倍数
secret_key = "ThisIs SecretKey" 
# 要加密的明文数据，长度必须是16的倍数
plain_data = "Hello, World123!"
# IV参数，长度必须是16的倍数
iv_param = 'This is an IV456'

# 数据加密
aes1 = AES.new(secret_key, AES.MODE_CBC, iv_param)
cipher_data = aes1.encrypt(plain_data)
print('cipher data：', cipher_data)

# 数据解密
aes2 = AES.new(secret_key, AES.MODE_CBC, 'This is an IV456')
plain_data2 = aes2.decrypt(cipher_data)  # 解密后的明文数据
print('plain text：', plain_data2)