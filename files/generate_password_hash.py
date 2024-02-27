import hashlib
import base64
import sys
from hashlib import pbkdf2_hmac

# Your new password
new_password = sys.argv[1]

# Salt - you can generate a new salt for each password
# Here, I'm using the same salt as in your previous example for consistency
salt = sys.argv[2]
decoded_salt = base64.b64decode(salt)

# Hashing parameters
hash_iterations = 27500
algorithm = 'sha256'

# Generating the hash for the new password
new_hash = pbkdf2_hmac(algorithm, new_password.encode(), decoded_salt, hash_iterations)

# Encoding the generated hash to a format similar to your secret data value
encoded_new_hash = base64.b64encode(new_hash).decode()

# The encoded hash
print(encoded_new_hash)
