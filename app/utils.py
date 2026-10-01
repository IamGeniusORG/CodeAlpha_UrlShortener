from nanoid import generate

def generate_short_code(size=8):
    """
    Generates a unique short code using nanoid.
    Uses a URL-safe alphabet (base62: a-z, A-Z, 0-9).
    """
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    return generate(alphabet, size)
