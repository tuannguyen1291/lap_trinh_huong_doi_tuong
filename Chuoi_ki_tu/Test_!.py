import random
danhsach = []
check = 0
for i in range(1000):
    danhsach.append(random.randint(-1000, 1000))
tenfile = input("Nhập tên file: ")
for i in danhsach:
    if check < 9:
        f = open(tenfile, 'a')
        chuoikytu = str(i)+','
        f.write(chuoikytu)
        f.close()
        check=check+1
    else:
        f = open(tenfile, 'a')
        f.write(str(i)+"\n" )
        f.close()
        check = 0
f = open(tenfile, 'r')
a = f.readlines()
for i in a:
    print(i.replace(",", "\t"))
f.close()