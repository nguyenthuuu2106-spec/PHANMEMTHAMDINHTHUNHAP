import streamlit as st

st.title("TÍNH CHỈ SỐ DTI")
st.write("Nhập thông tin khách hàng")

STV = st.number_input("Số tiền vay (VNĐ)", min_value=0, value=800_000_000, step=10_000_000)
THV = st.number_input("Thời hạn vay (năm)", min_value=1, value=5)
LS = st.number_input("Lãi suất vay (%/năm)", min_value=0.0, value=12.0, step=0.5)
TN = st.number_input("Thu nhập hàng tháng (VNĐ)", min_value=0, value=45_000_000, step=1_000_000)
NC = st.number_input("Nợ cũ hàng tháng (VNĐ)", min_value=0, value=10_000_000, step=1_000_000)
CPSH = st.number_input("Chi phí sinh hoạt/người (VNĐ)", min_value=0, value=4_000_000, step=500_000)
SN = st.number_input("Số người trong gia đình", min_value=1, value=3)

if st.button("TÍNH DTI"):
    if TN <= CPSH * SN:
        st.error("Thu nhập phải lớn hơn chi phí sinh hoạt gia đình!")
    else:
        DTI = (
            STV / (THV * 12)
            + STV * (LS / 100 / 12)
            + NC
        ) / (TN - CPSH * SN)

        st.metric("Chỉ số DTI", f"{DTI * 100:.2f}%")

        if DTI < 0.7:
            st.error("KẾT LUẬN: KHÔNG ĐƯỢC VAY")
        else:
            st.success("KẾT LUẬN: ĐƯỢC VAY")
