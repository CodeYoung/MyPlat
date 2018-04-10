from Crypto.Hash import SHA256

hash = SHA256.new()
hash.update('Hello, World!')
digest = hash.hexdigest()
print(digest)