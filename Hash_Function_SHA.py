import hashlib

def SHA1(cad):
    hashSHA1 = hashlib.sha1(cad.encode());
    resultSHA1 = hashSHA1.hexdigest()
    resultSHA1 = resultSHA1.upper()
    return resultSHA1

def SHA256(cad):
    
    hashSHA256 = hashlib.sha256(cad.encode());
    resultSHA256 = hashSHA256.hexdigest()
    resultSHA256 = resultSHA256.upper()
    return resultSHA256

# main();