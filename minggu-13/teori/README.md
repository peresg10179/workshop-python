
Apa yang baru
Mulai
Pelacak Isu
Lisensi
Pedoman Berkontribusi
DAPATKAN BUKUNYA
Python untuk Analisis Data
ALAT TERKAIT
SciPy
NumPy
Model Stats
scikit-belajar
Jupyter
matplotlib
Pustaka Analisis Data Python 
panda adalah open source, perpustakaan berlisensi BSD menyediakan kinerja tinggi,
 struktur data yang mudah digunakan dan alat analisis data untuk bahasa pemrograman Python .

panda adalah proyek yang disponsori NumFOCUS . 
Ini akan membantu memastikan keberhasilan pengembangan panda sebagai proyek sumber terbuka kelas dunia, 
dan memungkinkan untuk disumbangkan ke proyek

v0.23.4 Final (3 Agustus 2018) 
Ini adalah rilis minor perbaikan bug dalam seri 0.23.x dan mencakup beberapa perbaikan regresi, 
perbaikan bug, dan peningkatan kinerja. Kami menyarankan agar semua pengguna meningkatkan ke versi ini.

Rilis ini dapat diinstal dengan conda dari conda-forge atau saluran default

Atau melalui PyPI:


v0.23.4 (3 Agustus 2018)
Ini adalah rilis minor perbaikan bug dalam seri 0.23.x dan mencakup beberapa perbaikan regresi kecil dan perbaikan bug.
 Kami menyarankan agar semua pengguna meningkatkan ke versi ini.
 
 Apa yang baru di v0.23.4

Memperbaiki Regresi
Perbaikan kerusakan

Memperbaiki Regresi ¶
Python 3.7 dengan Windows memberikan semua nilai yang hilang untuk perhitungan varians bergulir ( GH21813 )

Perbaikan Bug 
Groupby / Resample / Rolling

Bug saat memanggil DataFrameGroupBy.agg()dengan daftar fungsi termasuk ohlcsebagai 
elemen non-awal akan memunculkan ValueError( GH21716 )
Bug dalam roll_quantilemenyebabkan kebocoran memori saat memanggil .rolling(...).
quantile(q)dengan qdalam (0,1) ( GH21965 )
Tidak ada

Bug di Series.clip()dan DataFrame.clip()tidak dapat menerima ambang seperti daftar yang berisi NaN( GH19992 )

v0.23.3 (7 Juli 2018) 
Rilis ini memperbaiki masalah build dengan sdist untuk Python 3.7 ( GH21785 ) Tidak ada perubahan lain.

v0.23.2 
Ini adalah rilis minor perbaikan bug dalam seri 0.23.x dan mencakup beberapa perbaikan regresi kecil dan perbaikan bug.
 Kami menyarankan agar semua pengguna meningkatkan ke versi ini.
 
 Pengurangan Logis atas Seluruh DataFrame ¶
DataFrame.all()dan DataFrame.any()sekarang menerima axis=Noneuntuk mengurangi dari semua sumbu ke skalar ( GH19976 )

ni juga menyediakan kompatibilitas dengan NumPy 1.15, yang sekarang dikirim ke DataFrame.all. Dengan NumPy 1.15 dan panda 0.23.1 atau lebih lama, 
numpy.all()tidak akan lagi mengurangi setiap sumbu:

Dengan panda 0.23.2, itu akan mengembalikan False dengan benar, seperti yang terjadi pada NumPy <1.15.

In [3]: np.any(pd.DataFrame({"A": [False], "B": [False]}))
Out[3]: False

Memperbaiki Regresi 
Memperbaiki regresi to_csv()ketika menangani objek seperti file secara tidak benar ( GH21471 )
Diizinkan ulang nama tingkat duplikat a MultiIndex. Mengakses level yang memiliki nama duplikat berdasarkan nama masih menimbulkan kesalahan ( GH19029 ).
Bug di keduanya DataFrame.first_valid_index()dan Series.first_valid_index()dibesarkan untuk indeks baris yang memiliki nilai duplikat ( GH21441 )
Memperbaiki pencetakan DataFrames dengan kolom hierarkis dengan nama panjang ( GH21180 )
Memperbaiki regresi dalam reindex()dan groupby() dengan MultiIndex atau beberapa kunci yang berisi nilai seperti waktu-kategoris ( GH21390 ).
Memperbaiki regresi dalam operasi negatif unary dengan objek tipe ( GH21380 )
Bug Timestamp.ceil()dan Timestamp.floor()ketika cap waktu merupakan kelipatan dari frekuensi pembulatan ( GH21262 )
Memperbaiki regresi dalam to_clipboard()yang default untuk menyalin dataframe dengan ruang terbatas bukan tab dibatasi ( GH21104 )

Bangun Perubahan 
Distribusi sumber dan biner tidak lagi menyertakan file data uji, menghasilkan ukuran unduhan yang lebih kecil. Tes yang mengandalkan file data ini akan dilewati saat menggunakan pandas.test(). ( GH19320 )
Perbaikan Bug 
Konversi

Bug saat membangun Indexdengan iterator atau generator ( GH21470 )
Bug masuk Series.nlargest()untuk dtip integer yang masuk dan tidak ditandatangani ketika nilai minimum ada ( GH21426 )
Pengindeksan

Bug Index.get_indexer_non_unique()dengan kunci kategoris ( GH21448 )
Bug dalam operasi perbandingan untuk MultiIndexkesalahan yang muncul pada perbandingan kesetaraan / ketidaksetaraan yang melibatkan MultiIndex dengan ( GH21149 )nlevels == 1
Bug dalam DataFrame.drop()perilaku tidak konsisten untuk indeks unik dan non-unik ( GH21494 )
Bug masuk DataFrame.duplicated()dengan sejumlah besar kolom menyebabkan 'kedalaman rekursi maksimum terlampaui' ( GH21524 ).
I / O

Bug di read_csv()yang menyebabkannya untuk benar meningkatkan kesalahan saat nrows=0, low_memory=Truedan index_coltidak None( GH21141 )
Bug json_normalize()saat memformat kolom record_prefixdengan bilangan bulat ( GH21536 )
Kategorikal

Bug dalam rendering Seriesdengan Categoricaldtype dalam kondisi langka di bawah Python 2.7 ( GH21002 )
Zona waktu

Bug di Timestampdan di DatetimeIndexmana melewati Timestamplokal setelah transisi DST akan mengembalikan datetime sebelum transisi DST ( GH20854 )
Bug dalam membandingkan kolom dengan transisi DST yang menghasilkan ( GH19970 )DataFrame`s with tz-aware :class:`DatetimeIndexKeyError
Timedelta

Bug di Timedeltamana timedelta non-nol yang lebih pendek dari 1 mikrodetik dianggap Salah ( GH21484 )


v0.23.1 
Ini adalah rilis minor perbaikan bug dalam seri 0.23.x dan mencakup beberapa perbaikan regresi kecil dan perbaikan bug. Kami menyarankan agar semua pengguna meningkatkan ke versi ini.

Memperbaiki Regresi 
Membandingkan Seri dengan datetime.date

Kami telah mengembalikan perubahan 0.23.0 untuk membandingkan data Seriesholding dan datetime.dateobjek ( GH21152 ). 
Dalam panda 0.22 dan sebelumnya, membandingkan Seri yang menyimpan datetimes dan datetime.dateobjek akan memaksa datetime.dateuntuk datetime sebelum comapring.
 Ini tidak konsisten dengan Python, NumPy, dan DatetimeIndex, yang tidak pernah mempertimbangkan datetime dan datetime.datesama.

Di 0.23.0, kami menyatukan operasi antara DatetimeIndex dan Seri, dan dalam proses itu mengubah perbandingan antara Seri data dan datetime.datetanpa peringatan.

Kami telah memulihkan sementara perilaku 0.22.0, jadi datetimes dan tanggal dapat kembali sama, tetapi mengembalikan perilaku 0.23.0 dalam rilis mendatang.

Untuk meringkas, inilah perilaku di 0.22.0, 0.23.0, 0.23.1:

Selain itu, perbandingan pemesanan akan meningkat TypeErrordi masa mendatang.

Perbaikan lainnya

Mengembalikan kemampuan to_sql()untuk melakukan sisipan multinilai karena ini menyebabkan regresi dalam kasus-kasus tertentu ( GH21103 ). Di masa depan ini akan dibuat dapat dikonfigurasi.
Memperbaiki regresi dalam DatetimeIndex.datedan DatetimeIndex.time atribut dalam hal data sadar zona waktu: DatetimeIndex.timemengembalikan waktu sadar-tz alih-alih naif ( GH21267 ) dan DatetimeIndex.date mengembalikan tanggal yang salah ketika tanggal input memiliki zona waktu non-UTC ( GH21230 ).
Memperbaiki regresi pandas.io.json.json_normalize()ketika dipanggil dengan Nonenilai dalam level bersarang di JSON, dan untuk tidak menjatuhkan kunci dengan nilai sebagai Tidak Ada ( GH21158 , GH21356 ).
Bug dalam to_csv()menyebabkan kesalahan pengodean saat kompresi dan pengodean ditentukan ( GH21241 , GH21118 )
Bug yang mencegah panda agar tidak dapat diimpor dengan optimasi -OO ( GH21071 )
Bug dalam Categorical.fillna()salah menaikkan nilaiTypeError ketika kategori individu dapat diubah dan nilai adalah dapat diubah ( GH21097 , GH19788 )
Memperbaiki regresi dalam konstruktor yang memaksa nilai-nilai NA suka Nonestring ketika lewat dtype=str( GH21083 )
Regresi di pivot_table()mana perintah Categoricaldengan nilai-nilai yang hilang untuk pivot indexakan memberikan hasil yang tidak selaras ( GH21133 )
Memperbaiki regresi dalam menggabungkan indeks / kolom boolean ( GH21119 ).

Peningkatan Kinerja 
Peningkatan kinerja CategoricalIndex.is_monotonic_increasing(), CategoricalIndex.is_monotonic_decreasing()dan CategoricalIndex.is_monotonic()( GH21025 )
Peningkatan kinerja CategoricalIndex.is_unique()( GH21107 )
Perbaikan Bug 
Groupby / Resample / Rolling

Bug di DataFrame.agg()mana menerapkan beberapa fungsi agregasi ke DataFramedengan nama kolom yang digandakan akan menyebabkan stack overflow ( GH21063 )
Bug di pandas.core.groupby.GroupBy.ffill()dan pandas.core.groupby.GroupBy.bfill()tempat pengisian dalam pengelompokan tidak akan selalu diterapkan sebagaimana dimaksud karena penggunaan implementasi jenis yang tidak stabil ( GH21207 )
Bug di pandas.core.groupby.GroupBy.rank()mana hasil tidak menskala hingga 100% saat menentukan method='dense'danpct=True
Bug di pandas.DataFrame.rolling()dan pandas.Series.rolling()yang menerima ukuran jendela 0 salah daripada menaikkan ( GH21286 )
Tipe data spesifik

Bug di Series.str.replace()mana metode melempar TypeError pada Python 3.5.2 ( GH21078 )
Bug di Timedelta: di mana melewati pelampung dengan unit akan secara prematur memutari presisi pelampung ( GH14156 )
Bug pandas.testing.assert_index_equal()yang AssertionErrorsalah mengangkat , saat membandingkan dua CategoricalIndexobjek dengan param check_categorical=False( GH19776 )
Jarang

Bug SparseArray.shapeyang sebelumnya hanya mengembalikan bentuk SparseArray.sp_values( GH21126 )
Pengindeksan

Bug di Series.reset_index()mana kesalahan yang sesuai tidak dimunculkan dengan nama level yang tidak valid ( GH20925 )
Bug interval_range()ketika start/ periodsatau end/ periodsditentukan dengan float startatau end( GH21161 )
Bug di MultiIndex.set_names()mana kesalahan muncul untuk MultiIndexdengan ( GH21149 )nlevels == 1
Bug dalam IntervalIndexkonstruktor yang membuat IntervalIndexdata dari kategori tidak didukung sepenuhnya ( GH21243 , GH21253 )
Bug MultiIndex.sort_index()yang tidak dijamin dapat disortir dengan benar level=1; ini juga menyebabkan ketidakselarasan data dalam DataFrame.stack()operasi tertentu ( GH20994 , GH20945 , GH21052 )
Merencanakan

Kata kunci baru (sharex, sharey) untuk mengaktifkan / menonaktifkan berbagi sumbu x / y oleh subplot yang dihasilkan dengan panda. DataFrame (). Groupby (). Boxplot () ( GH20968 )
I / O

Bug dalam metode IO menentukan compression='zip'yang menghasilkan arsip zip terkompresi ( GH17778 , GH21144 )
Bug DataFrame.to_stata()yang mencegah ekspor DataFrames ke buffer dan sebagian besar objek seperti file ( GH21041 )
Bug read_stata()dan StataReaderyang tidak mendekodekan string utf-8 dengan benar pada Python 3 dari Stata 14 file (dta versi 118) ( GH21244 )
Bug di IO JSON yang read_json()membaca skema JSON kosong dengan orient='table'kembali DataFramemenyebabkan kesalahan ( GH21287 )
Membentuk kembali

Bug concat()tempat kesalahan muncul dalam penyatuan Seriesdengan skalar dan nama tuple numpy ( GH21015 )
Bug dalam concat()pesan peringatan memberikan panduan yang salah untuk perilaku di masa mendatang ( GH21101 )
Lain

Tab selesai pada IndexIPython tidak lagi mengeluarkan peringatan penghentian ( GH21125 )
Bug yang mencegah panda digunakan pada Windows tanpa C ++ diinstal ulang ( GH21106 )
v0.23.0 (15 Mei 2018) 
Ini adalah rilis utama dari 0.22.0 dan termasuk sejumlah perubahan API, penghentian, fitur baru, peningkatan, dan peningkatan kinerja bersama dengan sejumlah besar perbaikan bug. Kami menyarankan agar semua pengguna meningkatkan ke versi ini.

Sorotan meliputi:

Format JSON round-trippable dengan orientasi 'table' .
Instansiasi dari dikte menghormati pesanan untuk Python 3.6+ .
Argumen kolom tergantung untuk ditugaskan .
Menggabungkan / menyortir pada kombinasi kolom dan level indeks .
Memperluas Panda dengan tipe khusus .
Tidak termasuk kategori yang tidak teramati dari groupby .
Perubahan untuk membuat bentuk output dari DataFrame.sangat konsisten .



