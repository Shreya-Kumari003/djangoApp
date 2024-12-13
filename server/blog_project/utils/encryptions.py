# # utils/encryption.py
# from cryptography.fernet import Fernet

# # Secret key (you should securely store this key, here it's hardcoded for simplicity)
# SECRET_KEY = b'your-secret-key-here'  # Use the key generated with Fernet.generate_key()

# def encrypt_token(token: str) -> str:
#     """Encrypt the token before sending to the client."""
#     f = Fernet(SECRET_KEY)
#     encrypted_token = f.encrypt(token.encode())
#     return encrypted_token.decode()

# def decrypt_token(encrypted_token: str) -> str:
#     """Decrypt the token after receiving from the client."""
#     f = Fernet(SECRET_KEY)
#     decrypted_token = f.decrypt(encrypted_token.encode())
#     return decrypted_token.decode()


# utils/encryption.py
# from cryptography.fernet import Fernet
# import os

# # Generate a key if it doesn't exist or retrieve it from environment variables
# def get_secret_key():
#     key = os.environ.get('FERNET_SECRET_KEY')
#     if key:
#         return key.encode()  # Return the key from the environment variable
#     else:
#         # If the key doesn't exist, generate one and return it (for the first time setup)
#         secret_key = Fernet.generate_key()
#         # Optionally, save this key securely to an environment variable or a config file
#         # For now, we'll just print it to the console (in production, save securely)
#         print(f"Generated Fernet key: {secret_key.decode()}")
#         return secret_key

# SECRET_KEY = get_secret_key()

# def encrypt_token(token: str) -> str:
#     """Encrypt the token before sending to the client."""
#     f = Fernet(SECRET_KEY)
#     encrypted_token = f.encrypt(token.encode())
#     return encrypted_token.decode()

# def decrypt_token(encrypted_token: str) -> str:
#     """Decrypt the token after receiving from the client."""
#     f = Fernet(SECRET_KEY)
#     decrypted_token = f.decrypt(encrypted_token.encode())
#     return decrypted_token.decode()


# from cryptography.fernet import Fernet
# import os

# # Generate or retrieve the secret key
# def get_secret_key():
#     key = os.environ.get('FERNET_SECRET_KEY')
#     if key:
#         return key.encode()
#     else:
#         secret_key = Fernet.generate_key()
#         print(f"Generated Fernet key: {secret_key.decode()}")
#         return secret_key

# SECRET_KEY = get_secret_key()

# def encrypt_token(token: str) -> str:
#     """Encrypt the token before sending to the client."""
#     f = Fernet(SECRET_KEY)
#     encrypted_token = f.encrypt(token.encode())
#     print(f"Encrypting Token: {token} -> {encrypted_token.decode()}")
#     return encrypted_token.decode()

# def decrypt_token(encrypted_token: str) -> str:
#     """Decrypt the token after receiving from the client."""
#     f = Fernet(SECRET_KEY)
#     decrypted_token = f.decrypt(encrypted_token.encode())
#     print(f"Decrypting Token: {encrypted_token} -> {decrypted_token.decode()}")
#     return decrypted_token.decode()
