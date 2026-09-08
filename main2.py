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
print("""
    This is an encryption program which uses the standard caesar encryption.
    Please enter the letter shift of your choice:
    """)

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

