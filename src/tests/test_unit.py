from utils import remove_non_letters, encode_url

def test_removing_numbers():
    assert remove_non_letters("http://localhost85") == "httplocalhost"
def test_removing_characters():
    assert remove_non_letters("http://localhost/(*#@&)") == "httplocalhost"
def test_removing_nothing():
    assert remove_non_letters("http://localhost/") == "httplocalhost"

def test_hashing():
    assert encode_url("http://localhost/") == "c9db56"
