from Crypto.Util.number import inverse


#Existential forgery
#public key = (9797,131)
n = 9797
e = 131

#x = s**e mod n
#Choose signature
s = 50

#Create message that is signed by the public key
message = pow(s, e, n)
print("Forged message:" + str(message))




