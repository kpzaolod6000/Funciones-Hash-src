import hashlib

def MD4(cad):
    hashObjectmd4 = hashlib.new('md4', cad.encode())
    resultmd4 = hashObjectmd4.hexdigest() 
    resultmd4 = resultmd4.upper()
    return resultmd4

def MD5(cad):
    hashObjectmd5 = hashlib.md5(cad.encode())
    resultmd5 = hashObjectmd5.hexdigest()
    resultmd5 = resultmd5.upper()
    return resultmd5

def main():
    cad = input()

    print("MD4 \t: ",MD4(cad))
    print("MD5 \t: ",MD5(cad))
# main();