import pickle
import sys
c=open(f"{sys.argv[1]}",'r')
m=open(f"{sys.argv[1]}_message.txt",'w')
k=open("decryption_key.dat",'rb')
decryption_key=pickle.load(k)
data=c.read()
message=''

for i in data:
    if i.isalpha():
        message+=decryption_key[i.upper()]
    else:
        message+=i

m.write(message)
m.flush()
m.close()
c.close()
k.close()
