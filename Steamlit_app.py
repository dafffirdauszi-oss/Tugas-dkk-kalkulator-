import streamlit as st

st.title("🔢 Aplikasi Kalkulator Sederhana")

# Input angka
angka1 = st.number_input("Masukkan angka pertama:", value=0.0)
angka2 = st.number_input("Masukkan angka kedua:", value=0.0)

# Pilih operasi
operasi = st.selectbox("Pilih operasi:", ["Tambah (+)", "Kurang (-)", "Kali (×)", "Bagi (÷)"])

# Tombol hitung
if st.button("Hitung"):
    if operasi == "Tambah (+)":
        hasil = angka1 + angka2

    elif operasi == "Kurang (-)":
        hasil = angka1 - angka2

    elif operasi == "Kali (×)":
        hasil = angka1 * angka2

    elif operasi == "Bagi (÷)":
        if angka2 == 0:
            st.error("❌ Tidak bisa membagi dengan nol!")
            hasil = None
        else:
            hasil = angka1 / angka2

    # Tampilkan hasil
    if hasil is not None:
        st.success(f"💡 Hasil: **{hasil}**")
