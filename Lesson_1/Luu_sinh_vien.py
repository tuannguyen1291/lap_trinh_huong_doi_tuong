from student import SinhVien
import os
import pickle
def ghi_doi_tuong(thumuc: str, tentaptin: str, obj: SinhVien):
    try:
        with open(os.path.join(thumuc,tentaptin),"wb") as f:
            pickle.dump(obj,f)
        print("Hoan thanh qua trinh ghi du lieu vao tap tin")
    except:
        print("Xay la loi")

