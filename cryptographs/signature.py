#public_key = (9797,131)(n,e)


#x = s**e mod n
#Choose signature

n = 9797
e = 131
s = 6292
s1 = 4768
s2 = 1424

x = s**e % n
x1 = s1**e % n
x2 = s2**e % n

print(x)
print(x1)
print("Only option c is valid signature: " + str(x2))
