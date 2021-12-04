import hmac
import hashlib
def HMAC(message,key,agl):
    resultHMAC = hmac.new(key.encode(), message.encode(), agl)
    resultHMAC = resultHMAC.hexdigest()
    resultHMAC = resultHMAC.upper()
    return resultHMAC