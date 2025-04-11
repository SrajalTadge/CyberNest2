
import base64

def custom_encrypt(message, key):
    try:
        # Step 1: Reverse message
        reversed_message = message[::-1]
        
        # Step 2: Offset characters using key
        offset = sum(ord(k) for k in key) % 256
        encrypted_chars = [chr((ord(char) + offset) % 256) for char in reversed_message]
        encrypted_str = ''.join(encrypted_chars)
        
        # Step 3: Encode to base64
        encrypted_base64 = base64.b64encode(encrypted_str.encode()).decode()
        return encrypted_base64
    except Exception as e:
        return f"Encryption error: {str(e)}"

def custom_decrypt(encoded_message, key):
    try:
        # Step 1: Decode from base64
        decoded_bytes = base64.b64decode(encoded_message)
        decoded_str = decoded_bytes.decode()
        
        # Step 2: Reverse offset
        offset = sum(ord(k) for k in key) % 256
        decrypted_chars = [chr((ord(char) - offset) % 256) for char in decoded_str]
        decrypted_str = ''.join(decrypted_chars)
        
        # Step 3: Reverse string
        original_message = decrypted_str[::-1]
        return original_message
    except Exception as e:
        return f"Decryption error: {str(e)}"
