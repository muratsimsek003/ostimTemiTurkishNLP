# streamlit_app.py

import streamlit as st
from temiturkishModel import main

def app_main():
    st.title("OSTIMTECH TEMI")

    # Buton oluşturma
    button_clicked = st.button("BANA SORU SOR")
    if button_clicked:
        st.write("ŞİMDİ KONUŞARAK SORU SORABİLİRSİNİZ")
        main()  # temiturkishModel.py dosyasındaki main fonksiyonunu çağır

if __name__ == "__main__":
    app_main()


#streamlit run streamlit_app.py

#(Created by Dr.Murat ŞİMŞEK)