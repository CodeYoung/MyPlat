from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as Signature_PKCS1_v1_5
message = "This is the message to send."
# 数据签名
with open('rsa.key', 'r') as f:
    private_key = f.read()
    rsa_key_obj = RSA.importKey(private_key)
    signer = Signature_PKCS1_v1_5.new(rsa_key_obj)
    digest = SHA.new()
    digest.update(message)
    signature = base64.b64encode(signer.sign(digest))
    print('signature text: ', signature)

# 验证签名
with open('rsa.pub', 'r') as f:
    public_key = f.read()
    rsa_key_obj = RSA.importKey(public_key)
    signer = Signature_PKCS1_v1_5.new(rsa_key_obj)
    digest = SHA.new(message)
    is_ok = signer.verify(digest, base64.b64decode(signature))
    print('is ok: ', is_ok)