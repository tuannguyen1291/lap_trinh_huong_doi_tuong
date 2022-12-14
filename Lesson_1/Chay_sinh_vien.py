from Luu_sinh_vien import ghi_doi_tuong
from Doc_tap_tin import doc_sinh_vien
from student import SinhVien
def main():
    path="D:\\cuong\\data"
    filename="sinhvien2.dat"
    sv1=SinhVien("Van Nhi",2004,10.0)
    ghi_doi_tuong(path,filename,sv1)
    noidung=doc_sinh_vien(path,filename)
    print(noidung)
    print("Ket thuc chuong trinh")
if __name__=="__main__":
    main()