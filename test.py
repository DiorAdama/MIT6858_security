import urllib.parse
import struct

s = "/"
with open("bugs.txt") as inj_f:
    for line in inj_f:
        s+=line
for i in range(10-1):
    s+="A"
s = urllib.parse.quote(s) + urllib.parse.quote(struct.pack("<I", 73621))


print(s)

