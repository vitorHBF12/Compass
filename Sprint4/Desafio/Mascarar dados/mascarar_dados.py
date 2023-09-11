import hashlib

while True:
    input_string = input("Digite uma string: ")
    hash_object = hashlib.sha1(input_string.encode())
    hex_dig = hash_object.hexdigest()
    print("SHA-1 Hash:", hex_dig)
