import collections

# 1. Menyiapkan Tabel Probabilitas
def hitung_probabilitas(teks):
    # Menghitung seberapa sering setiap karakter muncul
    jumlah_karakter = len(teks)
    frekuensi = collections.Counter(teks)
    
    # Membuat tabel rentang (interval) untuk setiap karakter
    probabilitas = {}
    titik_bawah = 0.0
    
    # Mengurutkan karakter agar konsisten
    for karakter in sorted(frekuensi.keys()):
        peluang = frekuensi[karakter] / jumlah_karakter
        # Setiap karakter punya 'jatah' rentang antara 0 sampai 1
        probabilitas[karakter] = (titik_bawah, titik_bawah + peluang)
        titik_bawah += peluang
        
    return probabilitas

# 2. Proses Enkripsi (Mengubah Teks menjadi Angka)
def enkripsi_aritmetik(teks, tabel_prob):
    bawah = 0.0
    atas = 1.0
    
    print(f"--- Proses Enkripsi: {teks} ---")
    
    for karakter in teks:
        rentang = atas - bawah
        bawah_karakter, atas_karakter = tabel_prob[karakter]
        
        # Perbarui batas atas dan bawah berdasarkan jatah karakter tersebut
        # Rumus: batas_baru = batas_lama_bawah + (rentang * jatah_karakter)
        atas = bawah + (rentang * atas_karakter)
        bawah = bawah + (rentang * bawah_karakter)
        
        print(f"Karakter '{karakter}' -> Rentang: [{round(bawah, 10)} ... {round(atas, 10)}]")
    
    # Hasil akhir adalah angka di tengah-tengah rentang terakhir
    return (bawah + atas) / 2

# 3. Proses Dekripsi (Mengubah Angka kembali menjadi Teks)
def dekripsi_aritmetik(angka_hasil, tabel_prob, panjang_teks):
    hasil_dekripsi = []
    
    print(f"\n--- Proses Dekripsi: {angka_hasil} ---")
    
    for _ in range(panjang_teks):
        for karakter, (bawah_karakter, atas_karakter) in tabel_prob.items():
            if bawah_karakter <= angka_hasil < atas_karakter:
                hasil_dekripsi.append(karakter)
                
                # Update angka untuk mencari karakter berikutnya
                rentang_karakter = atas_karakter - bawah_karakter
                angka_hasil = (angka_hasil - bawah_karakter) / rentang_karakter
                break
                
    return "".join(hasil_dekripsi)

# Data contoh: Pesan pendek karena keterbatasan presisi float pada komputer standar
data_input = "KOPI$" 
tabel = hitung_probabilitas(data_input)

# Tampilkan Tabel Jatah Rentang
print("Tabel Probabilitas Karakter:")
for k, v in tabel.items():
    print(f"'{k}': {v}")
print("-" * 40)

# Jalankan Enkripsi
kode_hasil = enkripsi_aritmetik(data_input, tabel)
print(f"\nHasil Akhir (Codeword): {kode_hasil}")

# Jalankan Dekripsi
teks_asli = dekripsi_aritmetik(kode_hasil, tabel, len(data_input))
print(f"Hasil Dekripsi: {teks_asli}")