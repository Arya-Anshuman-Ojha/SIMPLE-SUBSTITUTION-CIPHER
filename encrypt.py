import pickle
import sys
p=open(f"{sys.argv[1]}",'r')
c=open(f"{sys.argv[1]}_ciphertext.txt",'w')
k=open("encryption_key.dat",'rb')
encryption_key=pickle.load(k)
data=p.read()
ciphertext=''

for i in data:
    if i.isalpha():
        ciphertext+=encryption_key[i.upper()]
    else:
        ciphertext+=i

c.write(ciphertext)
c.flush()
c.close()
p.close()
k.close()
