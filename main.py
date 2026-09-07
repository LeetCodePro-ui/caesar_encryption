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
    letter_shift = input()
    try:
        letter_shift = int(letter_shift)
        break
    except ValueError:
        print("""
        ERROR:
        Enter a number!
              """)
        continue

shifting = {
        
        }


