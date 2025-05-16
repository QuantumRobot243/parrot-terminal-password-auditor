# password_strength.py

from hibp_checker import check_breaches
from entropy_calculator import calculate_entropy

def evaluate_password(password):
    """
    Evaluates the strength of a password and returns an HTML string
    with a CSS class for web display.
    """
    if len(password) < 8:
        return '<span class="weak">WEAK: Password too short (8+ required)</span>'
    
    if check_breaches(password):
        return '<span class="compromised">COMPROMISED: Found in multiple breaches</span>'
    
    entropy = calculate_entropy(password)
    if entropy < 50:
        return f'<span class="vulnerable">VULNERABLE: Low entropy ({entropy:.1f} bits)</span>'
    elif entropy < 80:
        return f'<span class="acceptable">ACCEPTABLE: Moderate entropy ({entropy:.1f} bits)</span>'
    else:
        return f'<span class="secure">SECURE: High entropy ({entropy:.1f} bits)</span>'
