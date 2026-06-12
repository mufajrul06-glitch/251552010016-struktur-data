import pandas as pd
import matplotlib.pyplot as plt

data = [
    {"tanggal": "2025-07-01", "warna": "merah", "ukuran": "S", "jumlah": 2, "harga": 10000},
    {"tanggal": "2025-07-01", "warna": "biru", "ukuran": "M", "jumlah": 15, "harga": 15000},
    {"tanggal": "2025-07-02", "warna": "merah", "ukuran": "L", "jumlah": 20, "harga": 20000},
    {"tanggal": "2025-07-02", "warna": "biru", "ukuran": "S", "jumlah": 25, "harga": 12000},
    {"tanggal": "2025-07-03", "warna": "merah", "ukuran": "M", "jumlah": 30, "harga": 18000},
    {"tanggal": "2025-07-03", "warna": "biru", "ukuran": "L", "jumlah": 35, "harga": 25000},
]

df = pd.DataFrame(data)
df["total"] = df["jumlah"] * df["harga"]

total_penjualan = df["total"].sum()

warna_order = ["merah", "putih", "biru"]
warna_terjual = df.groupby("warna")["jumlah"].sum().reindex(warna_order, fill_value=0)
total_kaos = warna_terjual.sum()

probabilitas = (warna_terjual / total_kaos) * 100

print("Total Penjualan selama 6 hari: Rp {:,.0f}". format(total_penjualan))
print("\nProbabilitas warna yang sering di beli:")
for warna, prob in probabilitas.items():
    print(f"Warna {warna}: {prob:.2f}%")

warna_ke_warna = {
    "merah": "red",
    "putih": "lightgray",
    "biru": "blue",
}
warna_grafik = [warna_ke_warna.get(warna, "gray") for warna in probabilitas.index]

plt.figure(figsize=(8, 5))
plt.bar(probabilitas.index, probabilitas.values, color=warna_grafik, edgecolor="black")
plt.title("Probabilitas Pembelian Kaos per Warna (6 Hari)")
plt.ylabel("Probabilitas (%)")
plt.xlabel("Warna")
plt.ylim(0, 50)
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

warna_data = list(zip(warna_terjual.index, warna_terjual.values))

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][1] < data[j + 1][1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

sorted_warna = bubble_sort(warna_data)

print("\nhasil pengurutan (Bubble Sort) bedasarkan jumlah terbanyak:")
for warna, jumlah in sorted_warna:
    print(f"{warna}: {jumlah} kaos")

plt.figure(figsize=(8, 5))
sorted_warna, sorted_jumlah = zip(*sorted_warna)
warna_grafik_sorted = ["red" if w == "merah" else "gray" if w == "putih" else "blue" for w in sorted_warna]

plt.bar(sorted_warna, sorted_jumlah, color=warna_grafik_sorted, edgecolor="black")
plt.title("Hasil bubble sort: warna kaos paling banyak terjual")
plt.ylabel("warna")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()