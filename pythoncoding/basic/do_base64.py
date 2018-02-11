import base64

def safe_base64_decode(s):
    n = len(s)
    m = n % 4
    s1 = base64.b64encode(s)