#!/usr/bin/python3
import zlib
import os

#Nomdu document a decoder (sans extension .lob) extrait du la table P_DOCUMENT_MEMO 
doc="compte-rendu"

blob_len=os.path.getsize(doc+".lob")
fs=open(doc+".lob", "rb")
blob=fs.read()
fs.close()


#Decodage blob
#  0x7F+0x01 -> 0x7F (=127)
#  0x7F+0x02 -> 0x1A (=26)
#  0x7F+0x03 -> 0x00 (=0)
#  sauf sur entete zlib 0x78+0x9C et checksum (4 bytes=ADLER32) final
i=j=0
#zblob_a: espace de travail pour decodage blob
zblob_a=bytearray(bytes(len(blob)))
while i<blob_len:
    #recopie tel quel l'entete et le checksum
    if i<2 or i>(len(blob)-4) or blob[i]!=127:
        zblob_a[j]=blob[i]
    else:
        n=blob[i+1]
        if n==1:
            zblob_a[j]=127
        elif n==2:
            zblob_a[j]=26
        elif n==3:
            zblob_a[j]=0
        i=i+1
    i=i+1
    j=j+1
#bytearray->bytes + reajustement taille blob
zblob=bytes(zblob_a[0:j])
#decompression zlib
rtf=zlib.decompress(zblob,0)

#enregistrement du RTF obtenu
fd=open(doc+".rtf","wb")
fd.write(rtf)
fd.close()

