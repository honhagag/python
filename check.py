import os

a= input("Nhập tên file: ")

os.mkdir(a)

with open(a,'w') as f:
    f.write("Te")
