# workshop-python

4. More Control Flow Tools
Selain pernyataan sementara yang baru saja diperkenalkan, Python mengetahui pernyataan aliran kontrol yang biasa dikenal dari bahasa lain

4.1. if Statements
Bisa ada nol atau lebih dari elif, dan bagian yang lain adalah opsional. Kata kunci ‘elif’ adalah singkatan dari ‘else if’, dan berguna untuk menghindari indentasi yang berlebihan. Sebuah jika ... elif ... elif ... urutan adalah pengganti untuk switch atau pernyataan kasus yang ditemukan dalam bahasa lain.

4.2. for Statements
Pernyataan  Python sedikit berbeda dari apa yang  Anda gunakan dalam C atau Pascal. Daripada selalu iterasi atas deret aritmetika angka (seperti dalam Pascal), atau memberikan pengguna kemampuan untuk menentukan baik langkah iterasi dan kondisi terputus (seperti C), Python untuk  iterasi atas item dari setiap urutan (daftar atau string), 

Jika  perlu memodifikasi urutan dengan melakukan iterasi saat berada di dalam loop (misalnya untuk menggandakan item yang dipilih), Anda disarankan untuk membuat salinan terlebih dahulu. Iterasi atas urutan tidak secara implisit membuat salinan.

4.3. The range() Function
Jika Anda perlu melakukan iterasi atas urutan angka, rentang fungsi bawaan () berguna.

Titik akhir yang diberikan tidak pernah menjadi bagian dari urutan yang dihasilkan, range (10) menghasilkan 10 nilai, indeks hukum untuk item dari urutan panjang 10

Dalam banyak hal objek dikembalikan oleh rentang (), itu bukan lah sebuah daftar,dalah objek yang mengembalikan item berurutan dari urutan yang diinginkan ketika Anda mengulanginya, ini bukanlah sebuah daftar jadi sangat menghemat ruang

4.4. break and continue Statements, and else Clauses on Loops
C, pecah dari bagian terluar untuk atau saat loop.

Pernyataan loop mungkin memiliki klausa lain; itu dieksekusi ketika loop berakhir .

Ketika digunakan dengan loop, klausul yang lain memiliki lebih banyak kesamaan dengan klausa lain dari pernyataan coba daripada yang dilakukannya jika pernyataan: klausa lain pernyataan coba berjalan ketika tidak ada pengecualian terjadi, dan klausa lain loop berjalan ketika tidak ada pemutusan terjadi 

4.5. pass Statements
Ini dapat digunakan ketika pernyataan diperlukan secara sintaksis tetapi program tidak memerlukan tindakan
 
4.6. Defining Functions
Pernyataan pertama dari badan fungsi dapat secara opsional berupa string literal; string literal ini adalah string dokumentasi fungsi, atau docstring. (Lebih lanjut tentang docstrings dapat ditemukan di bagian String Dokumentasi.) Ada alat-alat yang menggunakan docstrings untuk secara otomatis menghasilkan dokumentasi online atau dicetak, atau membiarkan pengguna secara interaktif menelusuri kode; itu adalah praktik yang baik untuk memasukkan aturan dalam kode yang Anda tulis, jadi biasakanlah.

Pelaksanaan fungsi memperkenalkan tabel simbol baru yang digunakan untuk variabel lokal fungsi. Lebih tepatnya, semua tugas variabel dalam fungsi menyimpan nilai dalam tabel simbol lokal; sedangkan referensi variabel pertama kali terlihat di tabel simbol lokal, kemudian di tabel simbol lokal melampirkan fungsi, kemudian di tabel simbol global, dan akhirnya di tabel nama built-in. Dengan demikian, variabel global tidak dapat secara langsung diberikan nilai dalam fungsi (kecuali disebutkan dalam pernyataan global), meskipun mereka dapat direferensikan.

Parameter aktual (argumen) ke pemanggilan fungsi diperkenalkan dalam tabel simbol lokal dari fungsi yang dipanggil ketika dipanggil; dengan demikian, argumen dilewatkan menggunakan panggilan oleh nilai (di mana nilai selalu merupakan referensi objek, bukan nilai objek). Ketika fungsi memanggil fungsi lain, tabel simbol lokal baru dibuat untuk panggilan itu.

4.7. More on Defining Functions
Juga dimungkinkan untuk mendefinisikan fungsi dengan sejumlah argumen variabel. Ada tiga bentuk, yang bisa digabungkan

4.7.1. Default Argument Values

Fungsi ini dapat dipanggil dengan beberapa cara:

hanya memberikan argumen wajib: ask_ok ('Apakah Anda benar-benar ingin berhenti?')
memberikan salah satu argumen opsional: ask_ok ('OK untuk menimpa file?', 2)
atau bahkan memberikan semua argumen: ask_ok ('OK untuk menimpa file?', 2, 'Ayolah, hanya ya atau tidak!')

4.7.2. Keyword Arguments

Dalam panggilan fungsi, argumen kata kunci harus mengikuti argumen posisional. Semua argumen kata kunci yang dilewatkan harus sesuai dengan salah satu argumen yang diterima oleh fungsi (misalnya aktor bukanlah argumen yang valid untuk fungsi burung beo), dan urutannya tidak penting. Ini juga termasuk argumen non-opsional (misalnya parrot (tegangan = 1000) juga valid). Tidak ada argumen yang dapat menerima nilai lebih dari satu kali. 

4.7.3. Arbitrary Argument Lists
opsi yang paling jarang digunakan adalah untuk menentukan bahwa suatu fungsi dapat dipanggil dengan sejumlah argumen acak. 

4.7.4. Unpacking Argument Lists
argumen sudah ada dalam daftar atau tupel tetapi perlu dibongkar untuk panggilan fungsi yang membutuhkan argumen posisi terpisah. Misalnya, fungsi rentang () built-in mengharapkan mulai terpisah dan menghentikan argumen. Jika tidak tersedia secara terpisah, tulis panggilan fungsi dengan * -operator untuk membongkar argumen dari daftar atau tupel

4.7.5. Lambda Expression
Fungsi anonim kecil dapat dibuat dengan kata kunci lambda. Fungsi ini mengembalikan jumlah dari dua argumennya: lambda a, b: a + b. Fungsi Lambda dapat digunakan di mana pun objek fungsi diperlukan. Mereka secara sintaksis terbatas pada satu ekspresi.

4.7.6. Documentation Strings

Baris pertama harus selalu berupa ringkasan singkat dan ringkas dari tujuan objek. Untuk keringkasan, itu tidak boleh secara eksplisit menyatakan nama atau jenis objek, karena ini tersedia dengan cara lain (kecuali jika nama yang terjadi adalah kata kerja yang menggambarkan operasi fungsi). Baris ini harus dimulai dengan huruf kapital dan diakhiri dengan titik.

Jika ada lebih banyak baris dalam string dokumentasi, baris kedua harus kosong, secara visual memisahkan ringkasan dari sisa deskripsi. Baris berikut harus berupa satu paragraf atau lebih yang menggambarkan konvensi pemanggilan objek, efek sampingnya, dll.

Pengurai Python tidak melonggarkan indentasi dari literal string multi-baris dengan Python, sehingga alat yang memproses dokumentasi harus melonggarkan indentasi jika diinginkan. Ini dilakukan dengan menggunakan konvensi berikut. Baris non-kosong pertama setelah baris pertama string menentukan jumlah indentasi untuk seluruh string dokumentasi. (Kita tidak dapat menggunakan baris pertama karena umumnya berdekatan dengan kutipan pembukaan string sehingga indentasinya tidak terlihat dalam string literal.) 

4.7.7. Function Annotations
Anotasi fungsi sepenuhnya informasi metadata opsional tentang jenis yang digunakan oleh fungsi yang ditentukan pengguna

Anotasi disimpan dalam atribut __annotations__ dari fungsi sebagai kamus dan tidak berpengaruh pada bagian lain dari fungsi. Anotasi parameter ditentukan oleh titik dua setelah nama parameter, diikuti oleh ekspresi yang mengevaluasi ke nilai anotasi. Anotasi pengembalian ditentukan oleh literal ->, diikuti oleh ekspresi, di antara daftar parameter dan tanda titik dua yang menunjukkan akhir pernyataan def. Contoh berikut memiliki argumen posisi, argumen kata kunci, dan nilai kembalian yang dianotasikan

4.8. Intermezzo: Coding Style

Gunakan 4-spasi indentasi, dan tidak ada tab.

4 ruang adalah kompromi yang baik antara lekukan kecil (memungkinkan kedalaman bersarang lebih besar) dan indentasi besar (lebih mudah dibaca). Tab memasukkan kebingungan, dan paling baik ditinggalkan.

Bungkus garis sehingga mereka tidak melebihi 79 karakter.

Ini membantu pengguna dengan layar kecil dan memungkinkan untuk memiliki beberapa file kode secara berdampingan pada layar yang lebih besar.

Gunakan baris kosong untuk memisahkan fungsi dan kelas, dan blok kode yang lebih besar di dalam fungsi.

Jika memungkinkan, berikan komentar pada garis mereka sendiri.

Gunakan docstring.

Gunakan spasi di sekitar operator dan setelah koma, tetapi tidak secara langsung di dalam konstruksi bracketing: a = f (1, 2) + g (3, 4).

Sebutkan kelas dan fungsi Anda secara konsisten; konvensi ini menggunakan CamelCase untuk kelas dan lower_case_with_underscores untuk fungsi dan metode. Selalu gunakan diri sebagai nama untuk argumen metode pertama (lihat A First Look at Classes untuk lebih lanjut tentang kelas dan metode).

Jangan menggunakan pengkodean mewah jika kode Anda dimaksudkan untuk digunakan di lingkungan internasional. Default Python, UTF-8, atau bahkan ASCII biasa berfungsi paling baik dalam hal apa pun.

Demikian juga, jangan gunakan karakter non-ASCII di pengidentifikasi jika hanya ada sedikit kesempatan orang yang berbicara bahasa yang berbeda akan membaca atau mempertahankan kode.
