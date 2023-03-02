import streamlit as st

st.title('GIẢI PHƯƠNG TRÌNH BẬC NHẤT')

a = float(st.number_input('Tham số a'))
b = float(st.number_input('Tham số b'))
ans = -b/a
if st.button('Giải'):
    st.success("Phương trình có 1 nghiệm là ", ans)
