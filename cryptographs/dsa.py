import hashlib



#DSA parameters p = 59, q = 29, a = 3
#Bobs private key d = 23, hash value h(x) = 2, ephemeral key kE = 13
#Key generation
p = 59
q = 29
a = 3
h = 2
kE = 13
d = 23

g=h**((p-1)/q)

#Bobs public key
y = (g**d) % p

# Creating digital signature
M = 5
r = ((g**kE)%p) % q
s = (1/kE*((M)+(d*r))) % q
signature = (r,s)

# Signature verification
w = (s**-1) % q
u1 = (M*w) % q
u2 = (r*w) % q
v = (((g**u1)*(y**u2)) % p) % q






