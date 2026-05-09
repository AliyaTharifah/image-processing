class Simpul:
    def __init__(self, frekuensi, simbol, kiri=None, kanan=None):
        self.frekuensi = frekuensi  # Jumlah kemunculan karakter
        self.simbol = simbol        # Karakter (misal: 'A', '1', atau ' ')
        self.kiri = kiri            # Jalur biner 0
        self.kanan = kanan          # Jalur biner 1
        self.arah_biner = ''        # Penanda bit (0/1)

kamus_kode = dict()

def Buat_Kamus_Kode(simpul, nilai_sekarang=''):
    kode_baru = nilai_sekarang + str(simpul.arah_biner)

    if simpul.kiri:
        Buat_Kamus_Kode(simpul.kiri, kode_baru)
    if simpul.kanan:
        Buat_Kamus_Kode(simpul.kanan, kode_baru)

    if not simpul.kiri and not simpul.kanan:
        kamus_kode[simpul.simbol] = kode_baru
    
    return kamus_kode

def Hitung_Kemunculan(data):
    # Menghitung frekuensi setiap karakter dalam teks
    daftar_frekuensi = dict()
    for karakter in data:
        if daftar_frekuensi.get(karakter) == None:
            daftar_frekuensi[karakter] = 1
        else:
            daftar_frekuensi[karakter] += 1
    return daftar_frekuensi

def Hitung_Efisiensi(data, hasil_kamus):
    # Membandingkan ukuran sebelum vs sesudah kompresi
    bit_awal = len(data) * 8  # 1 karakter dianggap 8 bit (standar ASCII)
    bit_akhir = 0
    
    for karakter in data:
        bit_akhir += len(hasil_kamus[karakter])
    
    print(f"Total Bit Awal: {bit_awal} bit")
    print(f"Total Bit Akhir: {bit_akhir} bit")
    print(f"Ruang yang dihemat: {round(100 - (bit_akhir/bit_awal*100), 2)}%")

def Kompresi_Huffman(teks):
    print(f"Data yang diproses: '{teks}'")
    
    # 1. Hitung frekuensi tiap karakter
    frekuensi_dict = Hitung_Kemunculan(teks)
    
    # 2. Masukkan setiap karakter ke dalam daftar objek Simpul
    daftar_simpul = []
    for s in frekuensi_dict:
        daftar_simpul.append(Simpul(frekuensi_dict[s], s))
    
    # 3. Bangun Pohon Huffman
    while len(daftar_simpul) > 1:
        # Urutkan simpul berdasarkan frekuensi terkecil
        daftar_simpul = sorted(daftar_simpul, key=lambda x: x.frekuensi)
        
        # Ambil dua simpul dengan frekuensi terendah
        simpul_kanan = daftar_simpul[0]
        simpul_kiri = daftar_simpul[1]
        
        # Beri label bit (kiri=0, kanan=1)
        simpul_kiri.arah_biner = 0
        simpul_kanan.arah_biner = 1
        
        # Gabungkan menjadi satu simpul induk baru
        induk_baru = Simpul(
            simpul_kiri.frekuensi + simpul_kanan.frekuensi,
            simpul_kiri.simbol + simpul_kanan.simbol,
            simpul_kiri,
            simpul_kanan
        )
        
        # Hapus dua anak dan tambahkan induknya ke daftar
        daftar_simpul.remove(simpul_kanan)
        daftar_simpul.remove(simpul_kiri)
        daftar_simpul.append(induk_baru)
    
    # 4. Buat Kamus Kode
    hasil_kamus = Buat_Kamus_Kode(daftar_simpul[0])
    print("\n--- Kamus Kode Huffman ---")
    for huruf in sorted(hasil_kamus):
        print(f"'{huruf}': {hasil_kamus[huruf]}")
    
    # 5. Hitung penghematan
    print("\n--- Analisis Ukuran ---")
    Hitung_Efisiensi(teks, hasil_kamus)
    
    # 6. Hasil Enkripsi
    hasil_akhir = "".join([hasil_kamus[k] for k in teks])
    return hasil_akhir, daftar_simpul[0]

def Dekompresi_Huffman(teks_biner, pohon):
    # Mengembalikan biner menjadi teks asli dengan menelusuri pohon
    hasil_teks = []
    simpul_saat_ini = pohon
    
    for bit in teks_biner:
        if bit == '1':
            simpul_saat_ini = simpul_saat_ini.kanan
        else:
            simpul_saat_ini = simpul_saat_ini.kiri
            
        # Jika sampai di daun, ambil simbolnya
        if not simpul_saat_ini.kiri and not simpul_saat_ini.kanan:
            hasil_teks.append(simpul_saat_ini.simbol)
            simpul_saat_ini = pohon # Kembali ke akar
            
    return "".join(hasil_teks)

# --- Eksekusi Program ---
input_data = "TEKNIK INFORMATIKA 2024"
teks_terkompresi, akar_pohon = Kompresi_Huffman(input_data)

print(f"\nString Biner: {teks_terkompresi}")
print(f"Data Kembali Asli: {Dekompresi_Huffman(teks_terkompresi, akar_pohon)}")