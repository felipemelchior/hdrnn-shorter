import re
import hashlib

def remove_non_letters(text: str) -> str:
    clean_text = re.sub(r'[^a-zA-Z]', '', text)
    print(clean_text)
    return clean_text

def encode_url(original_url: str) -> str:
    encoded_url = hashlib.md5(original_url.encode("ascii")).hexdigest()
    return encoded_url[:6]