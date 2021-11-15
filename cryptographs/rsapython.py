from Crypto.Util.number import inverse


n = 86609
e = 17

c = 12345 #encrypted message
p = 257
q = 337

phi = (p-1)*(q-1)

d = inverse(e,phi)
print(d)

m = (c**d)%n
print(m)

