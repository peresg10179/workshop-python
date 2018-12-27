Pembelajaran mesin: pengaturan masalah 
Secara umum, masalah pembelajaran mempertimbangkan sekumpulan n sampel data dan kemudian mencoba memprediksi properti dari data yang tidak diketahui. Jika setiap sampel lebih dari satu angka dan, misalnya, entri multi-dimensi (alias data multivarian ), dikatakan memiliki beberapa atribut atau fitur .
Masalah pembelajaran terbagi dalam beberapa kategori:
supervised learning , di mana datanya dilengkapi dengan atribut tambahan yang ingin kami prediksi ( Klik di sini untuk membuka halaman pembelajaran yang diawasi scikit-learn). Masalah ini dapat berupa:
oKlasifikasi : sampel milik dua kelas atau lebih dan kami ingin belajar dari data yang sudah diberi label cara memprediksi kelas data yang tidak berlabel. Contoh masalah klasifikasi adalah pengenalan digit tulisan tangan, di mana tujuannya adalah untuk menetapkan masing-masing vektor input ke salah satu dari sejumlah kategori diskrit. Cara lain untuk berpikir tentang klasifikasi adalah sebagai bentuk pembelajaran yang diawasi secara terpisah (sebagai lawan dari berkelanjutan) di mana seseorang memiliki jumlah kategori yang terbatas dan untuk masing-masing sampel yang disediakan, seseorang harus mencoba memberi label pada mereka dengan kategori atau kelas yang benar .
oregresi : jika output yang diinginkan terdiri dari satu atau lebih variabel kontinu, maka tugas itu disebut regresi . Contoh masalah regresi adalah prediksi panjang salmon sebagai fungsi dari umur dan beratnya.
pembelajaran tanpa pengawasan , di mana data pelatihan terdiri dari serangkaian vektor input x tanpa nilai target yang sesuai. Tujuan dalam masalah tersebut mungkin untuk menemukan kelompok contoh serupa dalam data, di mana disebut clustering , atau untuk menentukan distribusi data dalam ruang input, yang dikenal sebagai estimasi kepadatan , atau untuk memproyeksikan data dari dimensi tinggi. ruang ke dua atau tiga dimensi untuk tujuan visualisasi ( Klik di sini untuk pergi ke halaman Belajar Scikit-Belajar tanpa pengawasan).
Pelatihan dan set pengujian
Pembelajaran mesin adalah tentang mempelajari beberapa properti dari set data dan kemudian menguji properti tersebut terhadap set data lainnya. Praktek umum dalam pembelajaran mesin adalah untuk mengevaluasi suatu algoritma dengan membagi satu set data menjadi dua. Kami menyebut salah satu dari set itu set pelatihan , di mana kami mempelajari beberapa properti; kami menyebut set lainnya set pengujian , di mana kami menguji properti yang dipelajari.


Memuat contoh dataset 
scikit-learn dilengkapi dengan beberapa dataset standar, misalnya dataset iris dan digit untuk klasifikasi dan dataset harga rumah boston untuk regresi.
Berikut ini, kami memulai juru bahasa Python dari shell kami dan kemudian memuat irisdan digitsdataset. Konvensi notasi kami adalah yang $menunjukkan prompt shell sementara >>>menunjukkan prompt interpreter Python:



Dataset adalah objek seperti kamus yang menyimpan semua data dan beberapa metadata tentang data. Data ini disimpan di .dataanggota, yang merupakan array. Dalam kasus masalah yang diawasi, satu atau lebih variabel respon disimpan di anggota. Rincian lebih lanjut tentang set data yang berbeda dapat ditemukan di bagian khusus.n_samples, n_features.target
Misalnya, dalam kasus dataset digit, digits.datamemberikan akses ke fitur yang dapat digunakan untuk mengklasifikasikan sampel digit:


Belajar dan memprediksi 
Dalam kasus dataset digit, tugasnya adalah memprediksi, diberikan gambar, digit mana yang diwakilinya. Kami diberikan sampel masing-masing dari 10 kelas yang mungkin (digit nol hingga sembilan) di mana kami cocok dengan penduga untuk dapat memprediksi kelas yang termasuk dalam sampel yang tidak terlihat.
Dalam scikit-belajar, penduga untuk klasifikasi adalah objek Python yang mengimplementasikan metode dan .fit(X, y)predict(T)
Contoh estimator adalah kelas sklearn.svm.SVC, yang mengimplementasikan klasifikasi dukungan vektor . Konstruktor estimator menggunakan parameter model sebagai argumen.
Untuk saat ini, kami akan mempertimbangkan penduga sebagai kotak hitam:


Memilih parameter model
Dalam contoh ini, kami menetapkan nilai gammasecara manual. Untuk menemukan nilai bagus untuk parameter ini, kita bisa menggunakan alat seperti pencarian kisi dan validasi silang .
Contoh clfpenduga (untuk pengklasifikasi) pertama kali dipasang pada model; yaitu, ia harus belajar dari model. Ini dilakukan dengan melewati set pelatihan kami ke fitmetode. Untuk rangkaian pelatihan, kami akan menggunakan semua gambar dari dataset kami, kecuali untuk gambar terakhir, yang akan kami siapkan untuk prediksi kami. Kami memilih set pelatihan dengan [:-1]sintaks Python, yang menghasilkan array baru yang berisi semua kecuali item terakhir dari digits.data:


Sekarang Anda dapat memprediksi nilai baru. Dalam hal ini, Anda akan memprediksi menggunakan gambar terakhir dari digits.data. Dengan memprediksi, Anda akan menentukan gambar dari set pelatihan yang paling cocok dengan gambar terakhir.

Contoh lengkap masalah klasifikasi ini tersedia sebagai contoh yang dapat Anda jalankan dan pelajari: Mengenali angka tulisan tangan .
Ketekunan model 
Dimungkinkan untuk menyimpan model di scikit-learning dengan menggunakan model persistensi built-in Python, acar :


alam kasus khusus scikit-learn, mungkin lebih menarik untuk menggunakan pengganti joblib untuk acar ( joblib.dump& joblib.load), yang lebih efisien pada data besar tetapi hanya bisa acar ke disk dan bukan ke string:

Perhatikan bahwa acar memiliki beberapa masalah keamanan dan pemeliharaan. Silakan lihat bagian Ketekunan model untuk informasi lebih lanjut tentang ketekunan model dengan scikit-belajar.

Konvensi 
scikit-learn estimators mengikuti aturan tertentu untuk membuat perilakunya lebih prediktif. Ini dijelaskan secara lebih rinci dalam Daftar Istilah Ketentuan Umum dan Elemen API .

Ketik casting 

Di sini, kernel default rbfdiubah menjadi linearvia pertama SVC.set_params()setelah estimator dibuat, dan diubah kembali rbfuntuk mereparasi estimator dan membuat prediksi kedua.

Multiclass vs. multilabel fitting 
Saat menggunakan , tugas pembelajaran dan prediksi yang dilakukan tergantung pada format data target yang cocok:multiclass classifiers

Di sini, classifier berada fit() pada representasi label biner 2d dari y, menggunakan LabelBinarizer. Dalam hal ini predict()mengembalikan array 2d yang mewakili prediksi multilabel yang sesuai.

Perhatikan bahwa instance keempat dan kelima mengembalikan semua nol, yang menunjukkan bahwa mereka tidak cocok dengan ketiga label di fitatas. Dengan output multilabel, hal yang sama mungkin untuk sebuah instance untuk diberikan beberapa label:

Dalam hal ini, penggolongnya sesuai pada setiap instance yang diberi beberapa label. Ini MultiLabelBinarizerdigunakan untuk membuat binarize array 2d dari multilabel ke fitatas. Hasilnya, predict()mengembalikan array 2d dengan beberapa label yang diprediksi untuk setiap instance.



