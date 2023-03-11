import streamlit as st
import sklearn
import plotly

st.title('GIẢI PHƯƠNG TRÌNH BẬC NHẤT')

a = float(st.number_input('Tham số a'))
b = float(st.number_input('Tham số b'))
ans = -b
if st.button('Giải'):
    if a != 0:
        text = "Phương trình có 1 nghiệm là " + str(ans/a)
        st.success(text)
    if a == 0:
        st.error('Phương trình vô nghiệm')
    
