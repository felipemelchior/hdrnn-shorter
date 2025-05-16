import re
import hashlib

def encode_url(original_url: str) -> str:
    encoded_url = hashlib.md5(original_url.encode("ascii")).hexdigest()
    return encoded_url[:8]