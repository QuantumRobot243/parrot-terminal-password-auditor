# hibp_checker.py
import hashlib
import requests

def check_breaches(password):
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix = sha1_hash[:5]
    try:
        with requests.Session() as session:
            session.headers.update({'User-Agent': '[REDACTED] Scanner'})
            response = session.get(
                f"https://api.pwnedpasswords.com/range/{prefix}",
                timeout=5
            )
            return sha1_hash[5:] in response.text
    except Exception:
        return False
