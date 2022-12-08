from student import SinhVien
def main():
    sv=[SinhVien("Le Anh Duy",2004,10),
        SinhVien("HTNN",2005,11),
        SinhVien("Nguyen Thai Tuan",2004,10)]
    for items in sv:
        print(items)
if __name__=="__main__":
    main()