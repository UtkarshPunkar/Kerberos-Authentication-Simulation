import base64
import hashlib

# Hardcoded credentials (demo only)
USERS = {
    "alice": "password123",
    "bob": "mypassword",
    "utkarsh": "test123"
}

# Simulated keys
AS_TGS_KEY = "AS_TGS_SHARED_SECRET"
TGS_SS_KEY = "TGS_SS_SHARED_SECRET"

def encrypt(message, key):
    """Fake encryption using hashing + base64"""
    return base64.b64encode((message + key).encode()).decode()

def decrypt(cipher, key):
    """Fake decryption simulation"""
    try:
        decoded = base64.b64decode(cipher).decode()
        if decoded.endswith(key):
            return decoded.replace(key, "")
        return None
    except Exception:
        return None

def authenticate(username, password):
    """Step 1: Client → AS"""
    if username in USERS and USERS[username] == password:
        tgt = encrypt(username, AS_TGS_KEY)
        return tgt, AS_TGS_KEY
    return None, None

def generate_service_ticket(tgt, as_tgs_key):
    """Step 2: Client → TGS"""
    username = decrypt(tgt, as_tgs_key)
    if username:
        st = encrypt(username, TGS_SS_KEY)
        return st, TGS_SS_KEY
    return None, None

def access_service(st, tgs_ss_key):
    """Step 3: Client → Service Server"""
    username = decrypt(st, tgs_ss_key)
    if username:
        return f"✅ Access granted to {username} for the service!"
    return "❌ Access denied!"
