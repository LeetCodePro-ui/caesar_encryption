#encryption
banner = r"""
   _____                               ______                               _   _                      
  / ____|                             |  ____|                             | | (_)                     
 | |     __ _  ___  ___  __ _  _ __   | |__   _ __   ___  _ __ _   _ _ __  | |_ _  ___  _ __    
 | |    / _` |/ _ \/ __|/ _` || '__|  |  __| | '_ \ / __|| '__| | | | '_ \ | __| |/ _ \| '_ \   
 | |___| (_| |  __/\__ \ (_| || |     | |____| | | | (__ | |  | |_| | |_) || |_| | (_) | | | |  
  \_____\__,_|\___||___/\__,_||_|     |______|_| |_|\___||_|   \__, | .__/  \__|_|\___/|_| |_|  
                                                                __/ | |                            
                                                               |___/|_|                            
"""
print(banner)
print("\n\n")

while True:
    choice = input("""
    \nPlease enter your choice:
    :: 1:Encryption
    :: 2:Decryption\n""")

    try:
        choice = int(choice)
        if choice in [1,2]:
            break
        else:
            print("ERROR: Please enter a valid option.") 
    except ValueError:
        print("""
        ERROR:
        Enter a number!
        """)

        
print("""
    Please enter the letter shift of your choice:""")

while True:
   key = input()
   try:
        key = int(key)
        break
   except ValueError:
       print("""
       ERROR:
       Enter a number!
       """)



text = input("Please enter your text for encryption here:\n")
text = text.lower()

if choice == 1:
    print("\n--- Running Encryption ---")
    dictionary = {}

    for j in range(97, 123):
        digit = chr(j)
        enc_numb = (j - 97 + key)%26 + 97
        enc_let = chr(enc_numb)
        dictionary[digit] = enc_let




    encrypted_text = ""
    for i in text:

        if i == " ":
            encrypted_text += " "
        elif i == "!":
            encrypted_text += "!"
        elif i == ".":
            encrypted_text += "."
        elif i == ",":
            encrypted_text += ","
        else:
            encrypted_text += dictionary[i]

    print(f"Encrypted text:\n{encrypted_text}")


elif choice == 2:
    print("\n--- Running Decryption ---")
    dictionary = {}
    for x in range(97,123):
        digit = chr(x)
        dec_numb = (x - 97 - key)%26 + 97
        dec_let = chr(dec_numb)
        dictionary[digit] = dec_let

    decrypted_text = ""
    for k in text: 
        if k == " ":
            decrypted_text += " "
        elif k == "!":
            decrypted_text += "!"
        elif k == ".":
            decrypted_text += "."
        elif k == ",":
            decrypted_text += ","
        else:
            decrypted_text += dictionary[k]
    print(f"Decrypted text:\n{decrypted_text}")
