# affine-cipher
    Python module, that ensure text encrypting and decrypting with affine cipher.   

# Short documentation

    **encrypt()** method encrypts a string by Affine Chipher. 
    Also deletes special symboles like '!', '.', '<', '>', '_', '#', '-'
    Replaces sapaces with 'XMEZERAX
    
    


# Usage 

    text = "Hello, world!"
    encrypted = encrypt(text, 1, 3)
    decrypted = decrypt(encrypted, 1, 3)
    
    Output:
    
    encrypted: KHOORXMEZERAXZRUOG
    decrypted: HELLO, WORLD
    
    
    
    
