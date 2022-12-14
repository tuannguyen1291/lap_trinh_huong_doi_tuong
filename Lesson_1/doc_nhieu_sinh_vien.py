from student import SinhVien
import os
import pickle

def doc_sinh_vien(thumuc: str, tentaptin: str) -> SinhVien:
    try:
        with open(os.path.join(thumuc, tentaptin), "rb") as f:
            sv = pickle.load(f)
        return sv
    except Exception as e:
        return None

def ghi_doi_tuong(thumuc: str, tentaptin: str, objs: list[SinhVien]):
    try:
        with open(os.path.join(thumuc,tentaptin),"wb") as f:
            pickle.dump(objs,f)
        print("Hoan thanh qua trinh ghi du lieu vao tap tin")
    except:
        print("Xay la loi")
def in_list_sinh_vien(content: list[SinhVien]):
    for items in content:
        print(items)

def main():
    path="D:\\cuong\\data"
    filename="sinhvien2.dat"
    sv1=[SinhVien("Van Nhi",2004,10.0),
         SinhVien("Anh Duy",2004,10.0),
         SinhVien("Thai Tuan",2004,10.0)]
    ghi_doi_tuong(path,filename,sv1)
    noidung=doc_sinh_vien(path,filename)
    in_list_sinh_vien(noidung)
    print("Ket thuc chuong trinh")
if __name__=="__main__":
    main()