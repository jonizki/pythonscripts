alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


encrypted_word = [2,13,12,12,8,15,24,11,18,24,20,12,18]


def decryptor(start_point):
    string_decrypted = ""
    for letter in encrypted_word:
        position = alphabet[letter-start_point]
        string_decrypted += position
    print(string_decrypted)

for x in range(0,24):
    decryptor(x)


    
    



