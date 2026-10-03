import pickle
import sys
f=open(f"{sys.argv[1]}",'r')
w=open("ciphertext.txt",'w')
k=open("encryption_key.dat",'rb')
enkey=pickle.load(k)
data=f.read()
ciphertext=''

for i in data:
    if i.isalpha():
        ciphertext+=enkey[i.upper()]
    else:
        ciphertext+=i

w.write(ciphertext)
w.flush()
f.close()
k.close()
