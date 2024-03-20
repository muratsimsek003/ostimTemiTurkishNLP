# streamlit_app.py
import os
import streamlit as st
from temiturkishModel2 import temi_main


def main():
    st.title("OSTIMTECH TEMI")
    st.sidebar.image("logo.png", use_column_width=True)
    # Buton oluşturma
    button_clicked = st.button("BANA SORU SOR")
    if button_clicked:
        st.write("ŞİMDİ KONUŞARAK SORU SORABİLİRSİNİZ")
        temi_main()  # temiturkishModel.py dosyasındaki main fonksiyonunu çağır


if __name__ == "__main__":
    main()


#streamlit run streamlit_app.py

#(Created by Dr.Murat ŞİMŞEK)