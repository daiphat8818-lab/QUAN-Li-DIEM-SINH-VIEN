import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Quan ly diem sinh vien",
                   page_icon="📚",
                   layout="wide")

#1. Tao du lieu
data = {
    "Ho_ten": [
        
       "Le Dong Dai Phat", "Tran Van Binh",
        "Tran Le Hoang Long", "Pham Ngoc Bao",
        "Le Thien Minh", "Nguyen Trung Kien",
        "Nguyen Dinh Minh Quan", "Pham Xuan Hieu",
        "Tran Van Minh", "Tran Hoang Hai"    
],
    "Chuyen_can": [9, 8, 7, 10, 6, 8, 9, 7, 5, 8],
    "Giua_ky": [8, 7, 6, 9, 5, 8, 8, 6, 4, 7],
    "Cuoi_ky": [9, 8, 7, 9, 6, 9, 10, 7, 5, 8]
}

df = pd.DataFrame(data)

#2. Tinh diem tong ket
df["Tong_ket"] = (
    0.2 * df["Chuyen_can"]
    + 0.3 * df["Giua_ky"]
    + 0.5 * df["Cuoi_ky"]
).round(2)

#3. Xep loai
def xep_loai(diem):
    if diem >= 8.5:
        return "Gioi"
    elif diem >= 7:
        return "Kha"
    elif diem >= 5:
        return "Trung binh"
    return "Yeu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

#4. Tieu de va bang diem
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

bang = df.rename(columns={
    "Ho_ten": "Họ tên",
    "Chuyen_can": "Chuyên cần",
    "Giua_ky": "Giữa kỳ",
    "Cuoi_ky": "Cuối kỳ",
    "Tong_ket": "Tổng kết",
    "Xep_loai": "Xếp loại"
})

st.subheader("Bảng điểm sinh viên")
st.dataframe(bang, use_container_width=True)

#5. Thong ke
st.subheader("Thống kê kết quả")

c1, c2, c3 = st.columns(3)

c1.metric("Điểm trung bình",
          round(df["Tong_ket"].mean(), 2))

c2.metric("Số sinh viên đạt",
          int((df["Tong_ket"] >= 5).sum()))

c3.metric("Sĩ số lớp", len(df))

cao = df.loc[df["Tong_ket"].idxmax()]
thap = df.loc[df["Tong_ket"].idxmin()]

st.write("**Sinh viên cao điểm nhất:**",
         cao["Ho_ten"], "-", cao["Tong_ket"])

st.write("**Sinh viên thấp điểm nhất:**",
         thap["Ho_ten"], "-", thap["Tong_ket"])

#6. Chon sinh vien
st.subheader("Tra cứu điểm sinh viên")

ten = st.selectbox("Chọn sinh viên", df["Ho_ten"])
sv = df[df["Ho_ten"] == ten].iloc[0]

st.write("**Họ tên:**", sv["Ho_ten"])
st.write("**Chuyên cần:**", sv["Chuyen_can"])
st.write("**Giữa kỳ:**", sv["Giua_ky"])
st.write("**Cuối kỳ:**", sv["Cuoi_ky"])
st.write("**Điểm tổng kết:**", sv["Tong_ket"])
st.write("**Xếp loại:**", sv["Xep_loai"])

#7. Bieu do
st.subheader("Biểu đồ điểm tổng kết")

fig, ax = plt.subplots(figsize=(12, 5))
ax.bar(df["Ho_ten"], df["Tong_ket"])
ax.set_xlabel("Họ tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_ylim(0, 10)
plt.xticks(rotation=45, ha="right")
fig.tight_layout()

st.pyplot(fig)
plt.close(fig)

#8. Thong tin nguoi tao
st.markdown("---")
st.caption("Người tạo: [Lê Đồng Đại Phát] | MSSV: [038208020653]
