import argparse
from base64 import b64decode, b64encode
from Crypto.Cipher import AES

key = b64decode("")
iv = b64decode("")

def decrypt_data(encrypted_data):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.decrypt(encrypted_data)

def encrypt_data(data):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = _pad(data.encode())
    return cipher.encrypt(padded_data)

def _pad(s):
    block_size = AES.block_size
    return s + (block_size - len(s) % block_size) * bytes([block_size - len(s) % block_size])

def _unpad(s):
    return s[:-s[-1]]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Encrypt or decrypt data with AES CBC')
    parser.add_argument('data', help='the data to encrypt or decrypt')
    parser.add_argument('-e', '--encrypt', action='store_true', help='encrypt the data')
    parser.add_argument('-d', '--decrypt', action='store_true', help='decrypt the data')

    args = parser.parse_args()

    if args.encrypt and args.decrypt:
        print("Error: Only one of -e or -d can be specified.")
    elif not args.encrypt and not args.decrypt:
        print("Error: Either -e or -d must be specified.")
    elif args.encrypt:
        encrypted_data = encrypt_data(args.data)
        print(b64encode(encrypted_data).decode())
    else:
        encrypted_data = b64decode(args.data.encode())
        decrypted_data = decrypt_data(encrypted_data)
        print(_unpad(decrypted_data).decode())