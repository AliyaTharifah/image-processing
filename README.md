Proyek ini mendemonstrasikan tiga metode pengolahan data populer untuk kompresi dan pengelompokan informasi:

# 1. Huffman Encoding (Kompresi Teks)
Algoritma kompresi data lossless yang bekerja dengan cara memberikan kode biner lebih pendek untuk karakter yang sering muncul, dan kode lebih panjang untuk yang jarang muncul.

Fokus: Efisiensi penyimpanan berbasis frekuensi karakter.

Hasil: Mengurangi ukuran bit pada teks tanpa menghilangkan informasi asli.

# 2. K-Means Clustering (Pengelompokan Data)
Algoritma unsupervised learning yang mengelompokkan data ke dalam sejumlah k klaster. Setiap data akan masuk ke kelompok dengan pusat (centroid) terdekat.

Fokus: Segmentasi data dan penyederhanaan variasi (Kuantisasi).

Hasil: Peta koordinat yang terbagi menjadi beberapa zona kelompok yang saling terpisah.

# 3. Arithmetic Coding (Kompresi Berbasis Rentang)
Metode kompresi tingkat lanjut yang mengubah seluruh pesan menjadi satu bilangan pecahan tunggal antara 0 dan 1. Berbeda dengan Huffman, ia tidak membagi kode per karakter.

Fokus: Mencapai batas kompresi maksimal (Entropy) yang lebih optimal.

Hasil: Satu nilai desimal presisi tinggi yang mewakili satu rangkaian pesan utuh.
