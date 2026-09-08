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

#while True:
#   letter_shift = input()
#   try:
#        letter_shift = int(letter_shift)
#        break
#    except ValueError:
#        print("""
#        ERROR:
#        Enter a number!
#              """)
#        continue


dictionary = {
        "a":"b",
        "b":"c",
        "c":"d",
        "d":"e",
        "e":"f",
        "f":"g",
        "g":"h",
        "h":"i",
        "i":"j",
        "j":"k",
        "k":"l",
        "l":"m",
        "m":"n",
        "n":"o",
        "o":"p",
        "p":"q",
        "q":"r",
        "r":"s",
        "s":"t",
        "t":"u",
        "u":"v",
        "v":"w",
        "w":"x",
        "x":"y",
        "y":"z",
        "z":"a"
        }

text = input("Please enter your text for encryption here:\n")
text = text.lower()

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

