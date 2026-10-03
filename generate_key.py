#IMPORTING THE LIBRARIES====================================================================================================
import random
import pickle

#CREATING A RANDOM RELATION=================================================================================================
alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
shuffle=random.sample(alphabet,len(alphabet))

#DICTIONARIES FOR HOLDING THE ENCRYPTION AND DECRYPTION KEYS
encryption_key=dict()
decryption_key=dict()

#CREATING THE KEYS FROM THE RANDOM RELATION=================================================================================
for i in range(0,len(shuffle)):
    encryption_key[alphabet[i]]=shuffle[i]

pairs=list(dict.items(encryption_key))

for i in range(0,len(shuffle)):
    for j in range(0,len(shuffle)):
        if alphabet[i]==pairs[j][1]:
            decryption_key[alphabet[i]]=pairs[j][0]
            break

#WRITING THE KEYS INTO THE RESPECTIVE FILES=================================================================================
fe=open("encryption_key.dat",'wb')
fd=open("decryption_key.dat",'wb')
pickle.dump(encryption_key,fe)
pickle.dump(decryption_key,fd)
fe.flush()
fd.flush()
fe.close()
fd.close()
