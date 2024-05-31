from  Ceaser_cipher_logo import logo
print(logo)
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
,'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(start_text,shift_amount,cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
         shift_amount *=  -1    
    for char in  start_text:
        if char in letter:
            positon = letter.index(char)
            new_position = positon  + shift_amount  
            end_text += letter[new_position]
        else:
            end_text += char    
    print(f"The {cipher_direction}d text is {end_text}")
      
should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, or type'decode' to decrypt:\n")
    text = input("Please enter your text\n").lower()
    shift = int(input("Please type the number of shifts:\n"))
    shift = shift % 26
    
    ceaser(start_text = text , shift_amount = shift, cipher_direction = direction )      

    result = input("Do you want to encode or decode another word? Type 'Yes' or 'No'\n")
 
    if result == "no":
        should_end = True
    print("Arrivederci!! powering off")




"""def encrypt(plain_text,plain_shift):
        cipher_text = ""
        for l in plain_text:
            posistion = letter.index(l)
            new_position = posistion + plain_shift
            new_letter = letter[new_position]
            cipher_text+= new_letter
        print(f"The encoded text is {cipher_text}")    

    def decrypt(decrypt_text,decrypt_shift):
        plain_text = ""
        for l in decrypt_text:
            posistion = letter.index(l)
            new_position = posistion - decrypt_shift
            plain_text += letter[new_position]
        print(f"The encoded text is {plain_text}")    
        
    if direction == "encode": 
        encrypt(plain_text = text,plain_shift = shift)        
    elif direction == "decode":
        decrypt(decrypt_text = text,decrypt_shift = shift) """