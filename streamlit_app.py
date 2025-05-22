import streamlit as st

st.title("kucing lucu")
st.write(
    "kucing imut,bulu lebat [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.image("IMG20240203164859.jpg", width=200)

st.header("aplikasi mengecek nilai Genap/Ganjil")
angka= st.number_input("Tulis sebuah angka:", value=0,step=1)

if (angka % 2) ==0     
 st.write(f"{angka} adalah bilangan genap")
else
 st.write(f"{angka} adalah bilangan ganjil")
