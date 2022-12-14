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
