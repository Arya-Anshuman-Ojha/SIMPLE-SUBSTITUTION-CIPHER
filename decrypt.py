import pickle
import sys

k=open("decryption_key.dat",'rb')
decryption_key=pickle.load(k)
message=''

def process(data):
    global message
    for i in data:
        if i.isalpha():
            message+=decryption_key[i.upper()]
        else:
            message+=i

if sys.argv[1]=='file':
    c=open(f"{sys.argv[2]}",'r')
    m=open(f"{sys.argv[2][:3]}_message.txt",'w')
    data=c.read()
    process(data)
    m.write(message)
    m.flush()
    m.close()
    c.close()

elif sys.argv[1]=='text':
    data=sys.argv[2]
    process(data)
    print("\n\n\n",message,"\n\n\n")

k.close()
