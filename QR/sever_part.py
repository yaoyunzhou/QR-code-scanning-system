import rsa
import hashlib

# 生成密钥对
(public_key, private_key) = rsa.newkeys(512)

# 加密
def encrypt_file(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    encrypted_data = rsa.encrypt(data, public_key)
    with open(filename + '.enc', 'wb') as f:
        f.write(encrypted_data)

# 解密
def decrypt_file(filename):
    with open(filename, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = rsa.decrypt(encrypted_data, private_key)
    with open(filename[:-4], 'wb') as f:
        f.write(decrypted_data)

# 数字签名
def sign_file(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    signature = rsa.sign(data, private_key, 'SHA-256')
    with open(filename + '.sig', 'wb') as f:
        f.write(signature)

# 验证数字签名
def verify_signature(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    with open(filename + '.sig', 'rb') as f:
        signature = f.read()
    try:
        rsa.verify(data, signature, public_key)
        print('Digital signature is valid.')
    except rsa.VerificationError:
        print('Digital signature is invalid.')

# 加密文件
encrypt_file('file.dex')
encrypt_file('resources')
encrypt_file('file.xml')
encrypt_file('file.so')

# 数字签名
sign_file('file.dex')
sign_file('resources')
sign_file('file.xml')
sign_file('file.so')

# 验证数字签名
verify_signature('file.dex')
verify_signature('resources')
verify_signature('file.xml')
verify_signature('file.so')
