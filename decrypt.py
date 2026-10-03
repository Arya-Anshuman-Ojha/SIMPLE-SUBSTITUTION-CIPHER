import pickle
import sys
f=open(f"{sys.argv[1]}",'r')
w=open("message.txt",'w')
k=open("decryption_key.dat",'rb')
enkey=pickle.load(k)
data=f.read()
message=''

for i in data:
    if i.isalpha():
        message+=enkey[i.upper()]
    else:
        message+=i

w.write(message)
w.flush()
f.close()
k.close()
