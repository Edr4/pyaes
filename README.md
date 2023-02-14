# AES CBC Encryption/Decryption Script

This script allows you to encrypt or decrypt data using AES CBC encryption. It uses a key and initialization vector (IV) for encryption and decryption.

## Requirements

This script requires Python 3.x and the `pycryptodome` library. You can install it using `pip`:

```
pip install pycryptodome
```

## Usage

To use this script, you need to set the `key` and `iv` variables in the code to your own values before using it. 
You can find these variables near the top of the script:

```python
key = b64decode("")  # Your key here
iv = b64decode("")  # Your IV here
```

To encrypt data, run the script with the -e flag followed by the data you want to encrypt:

```python
python3 aes.py -e "my secret data"
```

To decrypt data, run the script with the -d flag followed by the base64-encoded encrypted data:

```python
python3 aes.py -d "WkGk97TzT6dHJ6qATc6wIw=="
```
