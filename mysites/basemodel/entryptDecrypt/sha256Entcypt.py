from Crypto.Hash import SHA256

hash = SHA256.new()
hash.update('Hello, World!'.encode('utf-8'))
digest = hash.hexdigest()
print(digest)