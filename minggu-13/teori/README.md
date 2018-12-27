10 Menit ke panda 
Ini adalah pengantar singkat untuk panda, terutama ditujukan untuk pengguna baru. Anda dapat melihat resep yang lebih kompleks di Cookbook .

Biasanya, kami mengimpor sebagai berikut:

Pembuatan Objek 
Lihat bagian Intro Struktur Data .

Membuat Seriesdengan melewati daftar nilai, membiarkan panda membuat indeks integer default

Membuat DataFramedengan melewatkan array NumPy, dengan indeks datetime dan label berlabel:
Menciptakan DataFramedengan melewatkan dict objek yang dapat dikonversi menjadi seperti seri.
Kolom yang dihasilkan DataFramememiliki dtypes yang berbeda .
Jika Anda menggunakan IPython, penyelesaian tab untuk nama kolom (serta atribut publik) secara otomatis diaktifkan. Berikut adalah subset dari atribut yang akan diselesaikan:

Seperti yang Anda lihat, kolom A, B, C, dan Dsecara otomatis tab selesai. Eada di sana juga; atribut lainnya telah dipotong untuk singkatnya

Melihat Data 
Lihat bagian Dasar - Dasar .

Berikut ini cara melihat baris atas dan bawah dari frame

Menampilkan indeks, kolom, dan data NumPy yang mendasarinya:

describe() memperlihatkan ringkasan statistik cepat dari data Anda:

Transpos data Anda

Menyortir berdasarkan sumbu:
Mengurutkan berdasarkan nilai:

Seleksi 
Catatan Sementara standar ekspresi Python / Numpy untuk memilih dan pengaturan yang intuitif dan berguna untuk bekerja interaktif, untuk kode produksi, kami merekomendasikan metode akses panda dioptimalkan data, .at, .iat, .locdan .iloc.
Lihat dokumentasi pengindeksan Pengindeksan dan Memilih Data dan MultiIndex / Pengindeksan Lanjut .

Mendapatkan 
Memilih satu kolom, yang menghasilkan Series, setara dengan df.A:
Memilih melalui [], yang mengiris baris.
Pilihan dengan Label 
Lihat lebih banyak di Seleksi oleh Label .

Untuk mendapatkan potongan melintang menggunakan label

Memilih pada multi-sumbu dengan label:

Menampilkan pengirisan label, kedua titik akhir disertakan :
Pengurangan dalam dimensi objek yang dikembalikan:
Untuk mendapatkan nilai skalar:
Untuk mendapatkan akses cepat ke skalar (setara dengan metode sebelumnya):
Seleksi berdasarkan Posisi 
Lihat lebih banyak di Seleksi oleh Posisi .

Pilih melalui posisi bilangan bulat yang dilewati:
Pengaturan ¶
Mengatur kolom baru secara otomatis menyelaraskan data dengan indeks.

Data Tidak Ada 
panda terutama menggunakan nilai np.nanuntuk mewakili data yang hilang. Secara default tidak termasuk dalam perhitungan. Lihat bagian Data Yang Hilang .

Reindexing memungkinkan Anda untuk mengubah / menambah / menghapus indeks pada sumbu yang ditentukan. Ini mengembalikan salinan data.

Operasi 
Lihat bagian Dasar pada Operasi Biner .

Statistik 
Operasi secara umum mengecualikan data yang hilang.

Melakukan statistik deskriptif:

Terapkan ¶
Menerapkan fungsi ke data:

Histogram ¶
Lihat lebih lanjut di Histogram dan Diskretisasi .
Metode String ¶
Seri dilengkapi dengan serangkaian metode pemrosesan string dalam atribut str yang membuatnya mudah dioperasikan pada setiap elemen array, seperti dalam cuplikan kode di bawah ini. Perhatikan bahwa pencocokan pola di str umumnya menggunakan ekspresi reguler secara default (dan dalam beberapa kasus selalu menggunakannya). Lihat lebih lanjut di Metode String Vektor .

Gabungkan 
Concat 
panda menyediakan berbagai fasilitas untuk dengan mudah menggabungkan bersama-sama Seri, DataFrame, dan objek Panel dengan berbagai jenis logika set untuk indeks dan fungsionalitas aljabar relasional dalam kasus operasi join / merge-type.

Lihat bagian Penggabungan .

Menggabungkan objek panda bersama dengan concat():

Bergabunglah ¶
Penggabungan gaya SQL. Lihat bagian penggabungan gaya Database .

Tambahkan 
Tambahkan baris ke bingkai data. Lihat bagian Tambah .
Pengelompokan 
Dengan "dikelompokkan berdasarkan", kami mengacu pada proses yang melibatkan satu atau lebih langkah-langkah berikut:

Membagi data menjadi beberapa kelompok berdasarkan beberapa kriteria
Menerapkan fungsi untuk setiap grup secara independen
Menggabungkan hasil ke dalam struktur data

Membentuk ulang 
Lihat bagian tentang Pengindeksan dan Pembentukan Ulang Hirarki .

Tumpukan 

Seri Waktu 
panda memiliki fungsi yang sederhana, kuat, dan efisien untuk melakukan operasi resampling selama konversi frekuensi (misalnya, mengubah data kedua menjadi data 5-menit). Ini sangat umum dalam, tetapi tidak terbatas pada, aplikasi keuangan. Lihat bagian Time Series 

Konversi antara periode dan cap waktu memungkinkan beberapa fungsi aritmatika yang nyaman untuk digunakan. Dalam contoh berikut, kami mengonversi frekuensi triwulanan dengan tahun yang berakhir pada November hingga 9 pagi di akhir bulan setelah akhir kuartal
Lihat bagian pada Tabel Pivot .

Kategorikal 
panda dapat memasukkan data kategorikal dalam a DataFrame. Untuk dokumen lengkap, lihat pengantar kategori dan dokumentasi API .

Merencanakan ¶
Lihat Plotting docs.

Mendapatkan Data Masuk / Keluar 
CSV 
Menulis ke file csv.
HDF5 
Membaca dan menulis ke HDFStores .

Menulis ke Toko HDF5.
Excel 
Membaca dan menulis ke MS Excel .

Menulis ke file excel.

Gotchas 
Jika Anda mencoba melakukan operasi, Anda mungkin melihat pengecualian seperti:

