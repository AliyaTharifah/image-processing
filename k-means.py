import numpy as np
import matplotlib.pyplot as plt

# 1. Menyiapkan Data Contoh (Koordinat Pelanggan)
# Misalkan x adalah posisi km arah Timur, y adalah arah Utara
def buat_data_pelanggan():
    # Membuat 3 kelompok data acak agar terlihat pola klasternya
    kelompok1 = np.random.randn(20, 2) + np.array([2, 2])
    kelompok2 = np.random.randn(20, 2) + np.array([8, 3])
    kelompok3 = np.random.randn(20, 2) + np.array([5, 8])
    
    data = np.vstack([kelompok1, kelompok2, kelompok3])
    return data

# 2. Inisialisasi Pusat Klaster (Centroid) secara Acak
def inisialisasi_pusat(data, k):
    # Mengambil k titik acak dari data sebagai pusat awal
    indeks_acak = np.random.permutation(data.shape[0])
    pusat = data[indeks_acak[:k]]
    return pusat

# 3. Menghitung Jarak Euclidean (Jarak Lurus)
def hitung_jarak(titik1, titik2):
    # Rumus: akar((x1-x2)^2 + (y1-y2)^2)
    return np.sqrt(np.sum((titik1 - titik2)**2))

# 4. Algoritma Utama K-Means
def jalankan_kmeans(data, k, iterasi=10):
    jumlah_sampel = data.shape[0]
    pusat = inisialisasi_pusat(data, k)
    label_klaster = np.zeros(jumlah_sampel)
    
    for i in range(iterasi):
        # Langkah A: Tahap Penugasan (Assigning)
        for j in range(jumlah_sampel):
            jarak_ke_pusat = []
            for p in pusat:
                jarak_ke_pusat.append(hitung_jarak(data[j], p))
            
            # Pilih pusat yang jaraknya paling dekat
            label_klaster[j] = np.argmin(jarak_ke_pusat)
            
        # Langkah B: Tahap Pembaruan (Updating)
        pusat_lama = pusat.copy()
        for klaster_id in range(k):
            # Ambil semua titik yang masuk ke klaster ini
            titik_klaster = data[label_klaster == klaster_id]
            
            # Hitung rata-rata posisi titik tersebut untuk jadi pusat baru
            if len(titik_klaster) > 0:
                pusat[klaster_id] = titik_klaster.mean(axis=0)
        
        # Jika pusat sudah tidak berubah, berhenti lebih awal
        if np.all(pusat_lama == pusat):
            print(f"Konvergensi tercapai pada iterasi ke-{i+1}")
            break
            
    return pusat, label_klaster

# 5. Visualisasi Hasil
def tampilkan_grafik(data, pusat, label, k):
    plt.figure(figsize=(8, 6))
    warna = ['red', 'blue', 'green', 'purple', 'orange']
    
    for i in range(k):
        # Gambar titik-titik data berdasarkan klasternya
        titik = data[label == i]
        plt.scatter(titik[:, 0], titik[:, 1], s=30, c=warna[i], label=f'Klaster {i+1}')
        
        # Gambar pusat klaster (tanda X besar)
        plt.scatter(pusat[i, 0], pusat[i, 1], s=200, c='yellow', marker='X', edgecolors='black')
        
    plt.title("Segmentasi Lokasi Pelanggan (K-Means)")
    plt.xlabel("Koordinat X (KM)")
    plt.ylabel("Koordinat Y (KM)")
    plt.legend()
    plt.grid(True)
    plt.show()

# membagi pelanggan ke dalam 3 wilayah distribusi (k=3)
K = 3
data_toko = buat_data_pelanggan()
pusat_akhir, label_akhir = jalankan_kmeans(data_toko, K)

print("Pusat klaster akhir (Koordinat Gudang):\n", pusat_akhir)
tampilkan_grafik(data_toko, pusat_akhir, label_akhir, K)