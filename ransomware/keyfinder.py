with open("Chrysanthemum.jpg","rb") as decrypted:
    with open("Chrysanthemum.jpg_encrypted","rb")as encrypted:
        encdata=encrypted.read()
        decdata=decrypted.read()
keyarray=[]
for i in range(33):
    keyarray.append(encdata[i]^decdata[i])
print(keyarray)