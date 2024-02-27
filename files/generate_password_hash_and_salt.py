#!/usr/bin/python3

import os, sys
import hashlib
import base64
from hashlib import pbkdf2_hmac

# Generate a new 16-byte salt
new_salt = os.urandom(16)
decoded_salt = new_salt  # Use this in the pbkdf2_hmac function

# Your new password
new_password = sys.argv[1]

# Hashing parameters
hash_iterations = 27500
algorithm = 'sha256'

# Generating the hash for the new password
new_hash = pbkdf2_hmac(algorithm, new_password.encode(), decoded_salt, hash_iterations)

# Encoding the generated hash to a format similar to your secret data value
encoded_new_salt = base64.b64encode(new_salt).decode()
encoded_new_hash = base64.b64encode(new_hash).decode()

# The encoded hash
print(encoded_new_salt)
print(encoded_new_hash)
