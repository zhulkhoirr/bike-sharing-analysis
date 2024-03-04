import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

day_df = pd.read_csv("https://raw.githubusercontent.com/zhulkhoirr/bike-sharing-analysis/master/dashboard/day.csv")
hour_df = pd.read_csv("https://raw.githubusercontent.com/zhulkhoirr/bike-sharing-analysis/master/dashboard/hour.csv")

with st.sidebar:
    st.write("Nama: Zhulkhoir Rifat Rianda Raja Faqih")
    st.write("Email: zhulkhoirrifat@gmail.com")
    
st.header("Bike Rental")

st.subheader("Jumlah Peminjam pada Setiap Jam")
result = hour_df.groupby(by="hr").instant.nunique().sort_index()

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(result.index, result.values, marker='o', linewidth=2, color="#82CAFF")
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Peminjam")
ax.set_xticks(result.index)
ax.tick_params(axis='x', which='major', labelsize=10)
ax.tick_params(axis='y', labelsize=10)

st.pyplot(fig)

with st.expander("Lihat Penjelasan"):
    st.write(
        """
        Dari jam 00.00 atau tengah malam sampai dini hari jam 03.00 mengalami penurunan peminjaman yang signifikan hanya 697 peminjam dan mulai kembali naik ketika pagi hari. Titik tertinggi peminjaman sepeda pada jam 16.00 dan jam 17.00 dengan 730 peminjam.
        """
    )
    
st.subheader("Jumlah Peminjam pada Setiap Musim (per hari)")
result = day_df.groupby(by="season").instant.nunique().sort_index().reset_index()

fig, ax = plt.subplots(figsize=(10, 6))

sns.barplot(
    y="instant",
    x="season",
    data=result,
    palette=["#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3"],
)
ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Peminjam")
ax.set_xticks(result.index)
ax.tick_params(axis='x', which='major', labelsize=10)
ax.tick_params(axis='y', labelsize=10)

st.pyplot(fig)
with st.expander("Lihat Penjelasan"):
    st.write(
        """
        - Kesimpulan dari pertanyaan kedua adalah peminatan tertinggi peminjam ada di summer atau musim panas dengan 188 peminjaman perhari dan yang terendah adalah musim gugur dengan 178 peminjaman.
        """
    )
