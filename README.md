# affine-cipher
    Python module, that ensure text encrypting and decrypting with affine cipher.   

# Short documentation

<h3> encrypt(text, a, b) </h3>
This method encrypts a string by Affine Chipher. 
Also deletes special symboles like '!', '.', '<', '>', '_', '#', '-'.
Replaces spaces with 'XMEZERAX'
    
<p>text: text that should be encrypted.</p>
<p>a, b: coefficients.</p>
returns: the encrypted text.
  
<h3> decrypt(text, a, b) </h3>

This method decrypts a string by Affine Chipher. 
<p>
text: text that should be decrypted.
</p>

<p>
a, b: coefficients.
</p>

<p>
returns: the decrypted text.
</p>



# Usage 

    text = "Hello, world!"
    encrypted = encrypt(text, 1, 3)
    decrypted = decrypt(encrypted, 1, 3)
    
    Output:
    
    encrypted: KHOORXMEZERAXZRUOG
    decrypted: HELLO, WORLD
    
    
    
    
