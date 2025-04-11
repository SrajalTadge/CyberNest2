
import base64
import codecs

# Base58 decoding map
BASE58_ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def base58_decode(s):
    num = 0
    for char in s:
        num *= 58
        if char not in BASE58_ALPHABET:
            raise ValueError("Invalid Base58 character: {}".format(char))
        num += BASE58_ALPHABET.index(char)
    return num.to_bytes((num.bit_length() + 7) // 8, 'big').decode('utf-8', errors='ignore')

def convert_base(text, base):
    try:
        if base == "base64":
            return base64.b64decode(text).decode()
        elif base == "base32":
            return base64.b32decode(text).decode()
        elif base == "base85":
            return base64.b85decode(text).decode()
        elif base == "hex":
            return bytes.fromhex(text).decode()
        elif base == "binary":
            return ''.join([chr(int(text[i:i+8], 2)) for i in range(0, len(text), 8)])
        elif base == "rot13":
            return codecs.decode(text, 'rot_13')
        elif base == "rot47":
            return ''.join([chr(33 + ((ord(char) - 33 + 47) % 94)) if 33 <= ord(char) <= 126 else char for char in text])
        elif base == "base58":
            return base58_decode(text)
        else:
            return "Unsupported base!"
    except Exception as e:
        return f"Error: {str(e)}"
