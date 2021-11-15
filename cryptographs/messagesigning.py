from Crypto.Util.number import inverse



#Bob public key (n,e) = (86609,17) with p = 257, q = 337
#Bobs private key:
p = 257
q = 337

n = p*q
phi = (p-1) * (q-1)
e = 17
d = inverse(e,phi)
#Private key = (86609,65777)
#Sending message
message = 12345
print("Original message: " + str(message))
#Bob sending the message using public key
encrypted = (12345**17) % 86609
print("Encrypted message: " + str(encrypted))
#Decryption using private key
decryption = (encrypted**65777) % 86609
print("Decrypted message: " + str(decryption))


