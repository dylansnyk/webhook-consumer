import hmac
import hashlib
import os

secret = os.environ.get("WEBHOOK_SECRET")

def verify_signature(request):

    byte_key = secret.encode()
    message = str(request.data).encode()
    
    digest = hmac.new( byte_key, message, hashlib.sha256 ).hexdigest()

    signature = f'sha256={digest}'

    print(signature)
    print(request.headers['x-hub-signature'])

    return signature == request.headers['x-hub-signature']
