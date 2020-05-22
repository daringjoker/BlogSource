keyarray=[110, 247, 155, 14, 69, 85, 94, 149, 150, 254, 171, 
117, 128, 180, 14, 64, 61, 245, 167, 27, 237, 213, 91, 128, 
169, 211, 141, 44, 184, 10, 64, 15, 110]
def decrypt(filename,key):
    with open(filename,"rb") as infile:
        for index,byte in enumerate(infile.read()):
            dbyte=byte ^ keyarray[index%32]
            print(chr(dbyte),end="")

decrypt("flag.txt_encrypted",keyarray)
        