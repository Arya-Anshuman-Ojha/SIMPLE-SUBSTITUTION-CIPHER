import pickle
import sys

k=open("encryption_key.dat",'rb')
encryption_key=pickle.load(k)
ciphertext=''

def process(data):
    global ciphertext
    for i in data:
        if i.isalpha():
            ciphertext+=encryption_key[i.upper()]
        else:
            ciphertext+=i

if sys.argv[1]=='file':
    p=open(f"{sys.argv[2]}",'r')
    c=open(f"{sys.argv[2][:3]}_ciphertext.txt",'w')
    data=p.read()
    process(data)
    c.write(ciphertext)
    c.flush()
    c.close()
    p.close()

elif sys.argv[1]=='text':
    data=sys.argv[2]
    process(data)
    print("\n\n\n",ciphertext,"\n\n\n")

k.close()
