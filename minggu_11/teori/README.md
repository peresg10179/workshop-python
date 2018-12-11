Project Layout

Buat direktori proyek dan masukkan:

Kemudian ikuti petunjuk instalasi untuk mengatur lingkungan virtual Python dan instal Flask untuk proyek Anda.

Tutorial akan menganggap Anda bekerja dari direktori flask-tutorial mulai sekarang.
 Nama file di bagian atas setiap blok kode relatif terhadap direktori ini.
 
 
Aplikasi Flask dapat sesederhana satu file.
 
 
Namun, karena proyek semakin besar, menjadi luar biasa untuk menyimpan semua kode dalam satu file.
 Proyek Python menggunakan paket untuk mengatur kode ke beberapa modul yang dapat diimpor jika diperlukan,
 dan tutorial akan melakukan ini juga
 
 Direktori proyek akan berisi:

flaskr /, paket Python yang berisi kode dan file aplikasi Anda.
tes /, direktori yang berisi modul uji.
venv /, lingkungan virtual Python tempat Flask dan dependensi lainnya dipasang.
Instalasi file yang memberitahukan Python cara menginstal proyek Anda.
Konfigurasi kontrol versi, seperti git. 
Anda harus membuat kebiasaan menggunakan beberapa jenis kontrol versi untuk semua proyek Anda,
 tidak peduli ukurannya.
File proyek lainnya yang mungkin Anda tambahkan di masa mendatang.
Pada akhirnya, tata letak proyek Anda akan terlihat seperti ini:


Jika Anda menggunakan kontrol versi, file-file berikut yang dihasilkan saat menjalankan proyek Anda harus diabaikan.
 Mungkin ada file lain berdasarkan editor yang Anda gunakan.
 Secara umum, abaikan file yang tidak Anda tulis. Misalnya, dengan git:
 
 The Application Factory
 
 
Aplikasi Flask adalah contoh kelas Flask. Segala sesuatu tentang aplikasi, 
seperti konfigurasi dan URL, akan terdaftar dengan kelas ini.

Cara paling mudah untuk membuat aplikasi Flask adalah membuat instance Flask global secara langsung di bagian atas kode Anda,
 seperti bagaimana contoh "Hello, World!" Muncul di halaman sebelumnya. 
Meskipun hal ini sederhana dan berguna dalam beberapa kasus,
 ini dapat menyebabkan beberapa masalah rumit ketika proyek tumbuh.

Daripada membuat instance Flask secara global, 
Anda akan membuatnya di dalam fungsi. Fungsi ini dikenal sebagai pabrik aplikasi. 
Setiap konfigurasi, pendaftaran, dan pengaturan lainnya yang dibutuhkan aplikasi akan terjadi di dalam fungsi,
maka aplikasi akan dikembalikan.
 

Pabrik Aplikasi
Saatnya mulai coding! Buat direktori flaskr dan tambahkan file __init__.py. __Init__.py melayani tugas ganda:
 ini akan berisi pabrik aplikasi,
 dan ini memberi tahu Python bahwa direktori flaskr harus diperlakukan sebagai paket.
 
 
create_app adalah fungsi pabrik aplikasi. Anda akan menambahkannya nanti di tutorial, tetapi sudah banyak.

app = Flask (__ name__, instance_relative_config = True) membuat instance Flask.
__name__ adalah nama modul Python saat ini. Aplikasi perlu tahu 
di mana lokasinya untuk menyiapkan beberapa jalur, dan __name__ adalah cara mudah untuk menceritakannya.
instance_relative_config = True memberitahu aplikasi bahwa file-file konfigurasi relatif terhadap folder instance.
 Folder instance terletak di luar paket flaskr dan dapat menyimpan data lokal yang tidak boleh dilakukan untuk kontrol versi,
 seperti rahasia konfigurasi dan file database.
app.config.from_mapping () menetapkan beberapa konfigurasi default yang akan digunakan aplikasi:
SECRET_KEY digunakan oleh Flask dan ekstensi untuk menjaga keamanan data.
 Ini disetel ke 'dev' untuk memberikan nilai yang mudah selama pengembangan,
 tetapi harus ditimpa dengan nilai acak saat penerapan.
DATABASE adalah jalur tempat file database SQLite akan disimpan.
 Ini di bawah app.instance_path, yang merupakan jalur yang dipilih Flask untuk folder instance. 
 Anda akan belajar lebih banyak tentang database di bagian selanjutnya.
app.config.from_pyfile () mengesampingkan konfigurasi default dengan nilai yang diambil dari file config.py 
dalam folder instance jika ada. Misalnya, saat menerapkan, ini dapat digunakan untuk menetapkan SECRET_KEY yang sebenarnya.
test_config juga dapat dikirimkan ke pabrik, dan akan digunakan sebagai pengganti konfigurasi instance.
 Ini agar tes yang akan Anda tulis nanti di tutorial dapat dikonfigurasi secara terpisah dari setiap nilai pengembangan yang telah Anda konfigurasikan.
os.makedirs () memastikan bahwa app.instance_path ada. 
Flask tidak membuat folder instance secara otomatis,
tetapi itu perlu dibuat karena proyek Anda akan membuat file database SQLite di sana.
@ app.route () membuat rute sederhana sehingga Anda dapat melihat aplikasi berfungsi sebelum masuk ke bagian tutorial lainnya.
 Ini menciptakan koneksi antara URL / hello dan fungsi yang mengembalikan respons, string 'Hello, World!' pada kasus ini.
Jalankan Aplikasi
Sekarang Anda dapat menjalankan aplikasi Anda menggunakan perintah flask.
 Dari terminal, beri tahu Flask di mana menemukan aplikasi Anda, lalu jalankan dalam mode pengembangan.

Mode pengembangan menunjukkan debugger interaktif setiap kali halaman memunculkan pengecualian, 
dan memulai ulang server setiap kali Anda membuat perubahan pada kode.
 Anda dapat membiarkannya berjalan dan cukup memuat ulang halaman browser saat Anda mengikuti tutorial.
 
 
 Define and Access the Database
 
 Aplikasi akan menggunakan database SQLite untuk menyimpan pengguna dan posting.
SQLite nyaman karena tidak memerlukan pengaturan server database terpisah dan terintegrasi dengan Python. 
Namun, jika permintaan bersamaan mencoba untuk menulis ke database pada saat yang sama,
 mereka akan melambat karena setiap penulisan terjadi secara berurutan.
 Aplikasi kecil tidak akan memperhatikan ini. Setelah Anda menjadi besar,
 Anda mungkin ingin beralih ke database yang berbeda.

Tutorial tidak membahas detail tentang SQL. Jika Anda tidak terbiasa dengannya, dokumen SQLite mendeskripsikan bahasa.

Hubungkan ke Database
Hal pertama yang harus dilakukan ketika bekerja dengan database SQLite 
(dan sebagian besar pustaka database Python lainnya) adalah membuat koneksi ke sana. 
Setiap pertanyaan dan operasi dilakukan menggunakan koneksi, yang ditutup setelah pekerjaan selesai.

Dalam aplikasi web, koneksi ini biasanya terkait dengan permintaan. 
Ini dibuat pada titik tertentu ketika menangani permintaan, dan ditutup sebelum respons dikirim.


g adalah objek khusus yang unik untuk setiap permintaan. Ini digunakan untuk menyimpan data yang mungkin diakses oleh beberapa fungsi selama permintaan.
 Sambungan disimpan dan digunakan kembali daripada membuat koneksi baru jika get_db dipanggil untuk kedua kalinya dalam permintaan yang sama.

current_app adalah objek khusus lain yang mengarah ke aplikasi Flask yang menangani permintaan.
 Karena Anda menggunakan pabrik aplikasi, tidak ada objek aplikasi saat menulis sisa kode Anda. 
get_db akan dipanggil ketika aplikasi telah dibuat dan menangani permintaan, sehingga current_app dapat digunakan.

sqlite3.connect () membuat koneksi ke file yang ditunjuk oleh kunci konfigurasi DATABASE.
 File ini belum ada, dan tidak akan sampai Anda menginisialisasi database nanti.

sqlite3.Row memberitahu koneksi untuk mengembalikan baris yang berperilaku seperti dicts.
 Ini memungkinkan mengakses kolom berdasarkan nama.

close_db memeriksa apakah koneksi dibuat dengan memeriksa apakah g.db telah diatur. Jika koneksi ada,
 itu sudah ditutup. 
 Lebih jauh ke bawah Anda akan memberitahu aplikasi Anda tentang fungsi close_db 
 di pabrik aplikasi sehingga dipanggil setelah setiap permintaan.

Buat Tabel
Di SQLite, data disimpan dalam tabel dan kolom. 
Ini perlu dibuat sebelum Anda dapat menyimpan dan mengambil data. 
Flaskr akan menyimpan pengguna di tabel pengguna, dan memposting di tabel pos.
 Buat file dengan perintah SQL yang diperlukan untuk membuat tabel kosong:
 
 
 
open_resource () membuka file relatif terhadap paket flaskr, yang berguna karena Anda tidak perlu tahu 
di mana lokasi itu ketika menerapkan aplikasi nanti.
 get_db mengembalikan koneksi database, yang digunakan untuk menjalankan perintah yang dibaca dari file.

click.command () mendefinisikan perintah baris perintah yang disebut init-db yang memanggil fungsi 
init_db dan menampilkan pesan sukses kepada pengguna.
 Anda dapat membaca Antarmuka Baris Perintah untuk mempelajari lebih lanjut tentang menulis perintah.

Mendaftar dengan Aplikasi
Fungsi close_db dan init_db_command harus terdaftar dengan instance aplikasi,
 jika tidak, mereka tidak akan digunakan oleh aplikasi. Namun, karena Anda menggunakan fungsi pabrik,
 instance itu tidak tersedia saat menulis fungsi.
 Sebaliknya, tulis suatu fungsi yang membutuhkan aplikasi dan melakukan pendaftaran.
 
 app.teardown_appcontext () memberi tahu Flask untuk memanggil fungsi itu ketika membersihkan setelah mengembalikan respons.

app.cli.add_command () menambahkan perintah baru yang dapat dipanggil dengan perintah flask.

Impor dan panggil fungsi ini dari pabrik. 
Tempatkan kode baru di akhir fungsi pabrik sebelum mengembalikan aplikasi.

flaskr / __ init__.py


Inisialisasi File Database
Sekarang init-db telah terdaftar dengan aplikasi,
 itu bisa disebut menggunakan perintah flask, mirip dengan perintah run dari halaman sebelumnya.

Catatan
Jika Anda masih menjalankan server dari halaman sebelumnya, 
Anda dapat menghentikan server, atau menjalankan perintah ini di terminal baru.
 Jika Anda menggunakan terminal baru, 
 jangan lupa untuk mengubah direktori proyek Anda dan aktifkan env seperti yang dijelaskan di Aktifkan lingkungan
. Anda juga harus menetapkan FLASK_APP dan FLASK_ENV seperti yang ditunjukkan pada halaman sebelumnya.

Blueprints dan Views
Fungsi tampilan adalah kode yang Anda tulis untuk menanggapi permintaan ke aplikasi Anda. Flask menggunakan pola untuk mencocokkan URL permintaan yang masuk ke tampilan yang harus menanganinya. 
Tampilan mengembalikan data yang Flask berubah menjadi respons keluar. Flask juga bisa pergi ke arah lain dan menghasilkan URL ke tampilan berdasarkan nama dan argumennya.

Buat Cetak Biru
Blueprint adalah cara untuk mengatur sekelompok pandangan terkait dan kode lainnya. 
Daripada mendaftarkan pandangan dan kode lain secara langsung dengan aplikasi,
 mereka terdaftar dengan cetak biru.
 Kemudian cetak biru terdaftar dengan aplikasi ketika tersedia dalam fungsi pabrik.

 
Flaskr akan memiliki dua cetak biru,
 satu untuk fungsi otentikasi dan satu lagi untuk fungsi posting blog.
 Kode untuk setiap cetak biru akan masuk dalam modul terpisah. 
 Karena blog perlu mengetahui tentang autentikasi, Anda akan menulis autentikasi terlebih dahulu.
 
 
Ini menciptakan Cetak Biru bernama 'auth'. Seperti objek aplikasi, cetak biru perlu tahu di mana itu didefinisikan, 
jadi __name__ dilewatkan sebagai argumen kedua. Url_prefix akan ditambahkan ke semua URL yang terkait dengan cetak biru.

Impor dan daftarkan blueprint dari pabrik menggunakan app.register_blueprint (). 
Tempatkan kode baru di akhir fungsi pabrik sebelum mengembalikan aplikasi.


Cetak biru autentikasi akan memiliki pandangan untuk mendaftarkan pengguna baru dan untuk masuk dan keluar.

Tampilan Pertama: Mendaftar
Ketika pengguna mengunjungi URL / auth / register, 
tampilan daftar akan mengembalikan HTML dengan formulir yang harus mereka isi. 
Ketika mereka menyerahkan formulir, 
itu akan memvalidasi masukan mereka dan menunjukkan formulir lagi dengan pesan kesalahan atau membuat pengguna baru dan pergi ke halaman login.

Untuk saat ini Anda hanya akan menulis kode tampilan.
 Di halaman berikutnya, Anda akan menulis template untuk menghasilkan formulir HTML.

flaskr / auth.py


Inilah yang dilakukan fungsi daftar tampilan:

@ bp.route mengaitkan URL / daftar dengan fungsi tampilan daftar. Ketika Flask menerima permintaan ke / auth / register, Flask akan memanggil tampilan register dan menggunakan nilai kembalian sebagai respons.

Jika pengguna mengirimkan formulir, request.method akan menjadi 'POST'. Dalam hal ini, mulailah memvalidasi input.

request.form adalah jenis khusus dari pemetaan teks yang dikirim dan nilai. Pengguna akan memasukkan nama pengguna dan kata sandinya.

Validasi bahwa nama pengguna dan kata sandi tidak kosong.

Validasi bahwa nama pengguna belum terdaftar dengan query database dan memeriksa jika hasilnya dikembalikan.
 db.execute mengambil kueri SQL dengan? 
 placeholder untuk setiap input pengguna, dan tuple nilai untuk menggantikan placeholder dengan. 
Pustaka basis data akan mengurus pelolosan nilai sehingga Anda tidak rentan terhadap serangan injeksi SQL.

fetchone () mengembalikan satu baris dari query. Jika query tidak mengembalikan hasil,
 ia mengembalikan None. Kemudian, fetchall () digunakan, yang mengembalikan daftar semua hasil.

Jika validasi berhasil, masukkan data pengguna baru ke dalam database. Untuk keamanan,
 kata sandi tidak boleh disimpan dalam basis data secara langsung. 
 Sebagai gantinya, generate_password_hash () digunakan untuk mengamankan hash kata sandi, dan hash itu disimpan. 
 Karena kueri ini memodifikasi data, db.commit () perlu dipanggil sesudahnya untuk menyimpan perubahan.

Setelah menyimpan pengguna, mereka diarahkan ke halaman login.
 url_for () menghasilkan URL untuk tampilan login berdasarkan namanya. 
 Ini lebih baik untuk menulis URL secara langsung karena ini memungkinkan Anda untuk mengubah URL nanti tanpa mengubah semua kode yang tertaut padanya.
 redirect () menghasilkan tanggapan redirect ke URL yang dihasilkan.

Jika validasi gagal, kesalahan ditampilkan kepada pengguna. 
flash () menyimpan pesan yang dapat diambil saat merender template.

Ketika pengguna awalnya menavigasi ke auth / register, atau ada kesalahan validasi,
 halaman HTML dengan formulir pendaftaran harus ditampilkan. render_template () akan membuat template yang berisi HTML,
 yang akan Anda tulis di langkah berikutnya dari tutorial.
 
 Pengguna ditanya terlebih dahulu dan disimpan dalam variabel untuk digunakan nanti.
check_password_hash () mencantumkan kata sandi yang dikirimkan dengan cara yang sama seperti hash yang disimpan dan membandingkannya dengan aman.
 Jika cocok, kata sandi valid.
sesi adalah perintah yang menyimpan data di seluruh permintaan. Ketika validasi berhasil, id pengguna disimpan di sesi baru
. Data disimpan dalam cookie yang dikirimkan ke browser, dan browser kemudian mengirimkannya kembali dengan permintaan berikutnya.
 Flask dengan aman menandatangani data sehingga tidak dapat dirusak.
Sekarang id pengguna disimpan dalam sesi, itu akan tersedia pada permintaan berikutnya. 
Di awal setiap permintaan, jika pengguna login di informasi mereka harus dimuat dan tersedia untuk tampilan lain.

flaskr / auth.py


bp.before_app_request () mendaftarkan fungsi yang berjalan sebelum fungsi tampilan
, tidak peduli apa URL yang diminta. load_logged_in_user memeriksa apakah id pengguna disimpan dalam sesi dan mendapatkan data pengguna tersebut dari database,
 menyimpannya di g.user, yang berlangsung selama lamanya permintaan. Jika tidak ada id pengguna,
 atau jika id tidak ada, g.user akan Tidak ada.

Keluar
Untuk keluar, Anda perlu menghapus id pengguna dari sesi. 
Kemudian load_logged_in_user tidak akan memuat pengguna pada permintaan berikutnya.

flaskr / auth.py


Dekorator ini mengembalikan fungsi tampilan baru yang membungkus tampilan asli yang diterapkan.
 Fungsi baru memeriksa apakah pengguna dimuat dan mengalihkan ke halaman masuk jika tidak
Jika pengguna dimuat, tampilan asli dipanggil dan berlanjut secara normal.
 Anda akan menggunakan dekorator ini saat menulis tampilan blog.

Endpoint dan URL
Fungsi url_for () menghasilkan URL ke tampilan berdasarkan nama dan argumen. 
Nama yang dikaitkan dengan tampilan juga disebut titik akhir, dan secara default sama dengan nama fungsi tampilan.

Misalnya, tampilan hello () yang ditambahkan ke pabrik aplikasi di awal tutorial memiliki nama 'hello' 
dan dapat ditautkan dengan url_for ('hello'). Jika butuh argumen, yang akan Anda lihat nanti, 
itu akan dikaitkan dengan menggunakan url_for ('hello', who = 'World').

Saat menggunakan cetak biru, nama cetak biru ditambahkan ke nama fungsi, 
jadi titik akhir untuk fungsi login yang Anda tulis di atas adalah 'auth.login'
 karena Anda menambahkannya ke cetak biru 'auth'
 
 
Template

Anda telah menulis tampilan autentikasi untuk aplikasi Anda,
 tetapi jika Anda menjalankan server dan mencoba membuka salah satu URL, 
 Anda akan melihat kesalahan TemplateNotFound. Itu karena tampilan memanggil render_template (), 
 tetapi Anda belum menulis template. File template akan disimpan dalam direktori templates di dalam paket flaskr.

Template adalah file yang berisi data statis serta placeholder untuk data dinamis.
 Sebuah template dirender dengan data spesifik untuk menghasilkan dokumen akhir.
 Flask menggunakan pustaka template Jinja untuk membuat templat.

Di aplikasi Anda, Anda akan menggunakan templat untuk merender HTML yang akan ditampilkan di browser pengguna.
 Di Flask, Jinja dikonfigurasi untuk membuat autoescape data apa pun yang diberikan dalam template HTML. 
 Ini berarti aman untuk merender input pengguna; setiap karakter yang mereka masukkan yang dapat mengacaukan HTML,
 seperti <dan> akan lolos dengan nilai aman yang terlihat sama di peramban tetapi tidak menyebabkan efek
 ng tidak diinginkan.

Jinja terlihat dan berperilaku seperti Python. 
Pembatas khusus digunakan untuk membedakan sintaks Jinja dari data statis dalam template.
 Apa pun di antara {{and}} adalah ekspresi yang akan dihasilkan ke dokumen akhir. 
 {% dan%} menunjukkan pernyataan aliran kontrol seperti jika dan untuk.
 Tidak seperti Python, blok dinotasikan dengan tag awal dan akhir 
 daripada indentasi karena teks statis dalam blok dapat mengubah indentasi.

Tata Letak Dasar
Setiap halaman dalam aplikasi akan memiliki tata letak dasar yang sama di sekitar tubuh yang berbeda.
Alih-alih menulis seluruh struktur HTML di setiap template,
 setiap template akan memperluas template dasar dan menimpa bagian tertentu.
 
 Static Files
 
 Tampilan dan templat autentikasi berfungsi, tetapi tampilannya sangat jelas sekarang. 
 Beberapa CSS dapat ditambahkan untuk menambahkan gaya ke tata letak HTML yang Anda buat. Gaya tidak akan berubah, 
 jadi ini adalah file statis daripada template.

Flask secara otomatis menambahkan pandangan statis yang mengambil jalur relatif ke direktori flaskr / statis dan menyajikannya.
 Template base.html sudah memiliki tautan ke file style.css:
 
 Selain CSS, jenis file statis lainnya mungkin berupa file dengan fungsi JavaScript, atau gambar logo
 . Mereka semua ditempatkan di bawah direktori flaskr / statis dan direferensikan dengan url_for ('statis', filename = '...').

Tutorial ini tidak berfokus pada cara menulis CSS, jadi Anda cukup menyalin yang berikut ini ke file flaskr / static / style.css:
flaskr / static / style.css

Anda dapat menemukan versi style.css yang kurang ringkas dalam kode contoh.

Pergi ke http://127.0.0.1:5000/auth/login dan halaman akan terlihat seperti screenshot di bawah ini

Anda dapat membaca lebih lanjut tentang CSS dari dokumentasi Mozilla. Jika Anda mengubah file statis, segarkan halaman browser. 
Jika perubahan tidak muncul, coba kosongkan cache browser Anda

Blog Blueprint

Anda akan menggunakan teknik yang sama yang Anda pelajari saat menulis cetak biru autentikasi untuk menulis cetak biru blog.
 Blog harus mencantumkan semua posting, memungkinkan pengguna login untuk membuat posting, dan memungkinkan penulis posting untuk mengedit atau menghapusnya.

Saat Anda menerapkan setiap tampilan, biarkan server pengembangan berjalan. Saat Anda menyimpan perubahan,
 coba buka URL di browser Anda dan uji coba.
Blueprint

Tentukan cetak biru dan daftarkan di pabrik aplikasi.
flaskr / blog.py

Impor dan daftarkan blueprint dari pabrik menggunakan app.register_blueprint (). Tempatkan kode baru di akhir fungsi pabrik sebelum mengembalikan aplikasi.
Tidak seperti cetak biru auth, cetak biru blog tidak memiliki url_prefix. Jadi tampilan indeks akan berada di /,
 tampilan buat di / create, dan seterusnya. Blog adalah fitur utama Flaskr, jadi masuk akal bahwa indeks blog akan menjadi indeks utama.

Namun, titik akhir untuk tampilan indeks yang didefinisikan di bawah ini adalah blog.index. Beberapa pandangan otentikasi mengacu pada titik akhir indeks biasa.
 app.add_url_rule () mengaitkan nama akhir 'index' dengan / url sehingga url_for ('index') atau url_for ('blog.index') akan berfungsi, menghasilkan URL yang sama.

Di aplikasi lain, Anda mungkin memberikan blog blueprint url_prefix dan menentukan tampilan indeks terpisah di pabrik aplikasi, mirip dengan tampilan hello.
 Maka indeks dan blog.index endpoint dan URL akan berbeda.
Indeks

Indeks akan menampilkan semua posting, yang paling baru pertama. A JOIN digunakan sehingga informasi penulis dari tabel pengguna tersedia dalam hasil.
flaskr / blog.py

Ketika seorang pengguna login, blok header menambahkan tautan ke tampilan buat. Saat pengguna adalah penulis pos,
 mereka akan melihat tautan "Edit" ke tampilan pembaruan untuk pos tersebut. loop.last adalah variabel khusus yang tersedia di dalam Jinja untuk loop. 
 Ini digunakan untuk menampilkan garis setelah setiap kiriman kecuali yang terakhir, untuk memisahkannya secara visual.
Membuat

Tampilan buat berfungsi sama dengan tampilan daftar autentikasi. Entah formulir ditampilkan,
 atau data yang diposting divalidasi dan posting ditambahkan ke database atau kesalahan ditampilkan.

Dekor login_required yang Anda tulis sebelumnya digunakan pada tampilan blog.
 Pengguna harus masuk untuk mengunjungi pandangan ini, jika tidak mereka akan dialihkan ke halaman login.
 
 Memperbarui

Baik tampilan pembaruan dan penghapusan akan perlu mengambil posting oleh id dan memeriksa apakah penulis cocok dengan pengguna yang masuk. Untuk menghindari duplikasi kode,
 Anda dapat menulis fungsi untuk mendapatkan pos dan memanggilnya dari setiap tampilan.
 
 kembalikan pos

batalkan () akan menaikkan pengecualian khusus yang mengembalikan kode status HTTP. Diperlukan pesan opsional untuk ditampilkan dengan kesalahan, 
jika tidak, pesan default digunakan. 404 berarti "Tidak Ditemukan", dan 403 berarti "Dilarang". (401 berarti "Tidak sah",
 tetapi Anda mengalihkan ke halaman masuk bukannya mengembalikan status itu.)

Argumen check_author didefinisikan sehingga fungsi tersebut dapat digunakan untuk mendapatkan pos tanpa memeriksa penulisnya.
 Ini akan berguna jika Anda menulis tampilan untuk menampilkan pos individual di halaman, di mana pengguna tidak menjadi masalah karena mereka tidak memodifikasi pos.
 
 Tidak seperti pandangan yang Anda tulis sejauh ini, fungsi pembaruan mengambil argumen, id. Itu sesuai dengan <int: id> di rute. URL nyata akan terlihat seperti / 1 / pembaruan. Flask akan menangkap 1,
 memastikan itu int, dan menyebarkannya sebagai argumen id. Jika Anda tidak menentukan int: dan sebagai gantinya lakukan <id>, ini akan menjadi string.
 Untuk menghasilkan URL ke halaman pembaruan, url_for () perlu dilewatkan id sehingga tahu apa yang harus diisi: url_for ('blog.update', id = posting ['id']). 
 Ini juga ada di file index.html di atas.

Tampilan buat dan perbarui terlihat sangat mirip. Perbedaan utama adalah bahwa tampilan pembaruan menggunakan objek pos dan kueri UPDATE, bukan INSERT.
 Dengan beberapa refactoring pintar, Anda bisa menggunakan satu tampilan dan template untuk kedua tindakan, tetapi untuk tutorialnya lebih jelas untuk memisahkannya.
 
 Template ini memiliki dua bentuk. Posting pertama data yang diedit ke halaman saat ini (/ <id> / update). 
 Bentuk lainnya hanya berisi tombol dan menentukan atribut tindakan yang memposting ke tampilan hapus.
 Tombol ini menggunakan beberapa JavaScript untuk menampilkan dialog konfirmasi sebelum mengirimkan.

Pola {{request.form ['title'] atau post ['title']}} digunakan untuk memilih data apa yang muncul dalam formulir. Ketika formulir belum dikirim,
 data postingan asli muncul, tetapi jika data formulir yang tidak valid dikirim, Anda ingin menampilkan itu sehingga pengguna dapat memperbaiki kesalahan, 
 jadi request.form digunakan sebagai gantinya. permintaan adalah variabel lain yang secara otomatis tersedia dalam template.
Menghapus

Tampilan hapus tidak memiliki templatnya sendiri, tombol hapus adalah bagian dari update.html dan posting ke URL / <id> / hapus.
 Karena tidak ada template, itu hanya akan menangani metode POST kemudian mengarahkan ke tampilan indeks.
 
 Make the Project Installable
 
 Membuat proyek Anda dapat diinstal berarti Anda dapat membuat file distribusi dan memasangnya di lingkungan lain,
 seperti Anda memasang Flask di lingkungan proyek Anda. 
 Ini membuat penerapan proyek Anda sama dengan memasang pustaka lain,
 jadi Anda menggunakan semua alat Python standar untuk mengelola semuanya.

Instalasi juga dilengkapi dengan manfaat lain yang mungkin tidak jelas dari tutorial atau sebagai pengguna Python baru, termasuk:

    -Saat ini, Python dan Flask memahami cara menggunakan paket flaskr hanya karena Anda menjalankan dari direktori proyek Anda.
	Memasang berarti Anda dapat mengimpornya dari mana pun Anda lari.
    -Anda dapat mengelola dependensi proyek Anda seperti yang dilakukan paket lain, sehingga pip instal proyek Anda.yang menginstalnya.
    -Alat uji dapat mengisolasi lingkungan pengujian Anda dari lingkungan pengembangan Anda.
	


Catatan

Ini sedang diperkenalkan di akhir tutorial, tetapi dalam proyek masa depan Anda, Anda harus selalu mulai dengan ini.


paket memberi tahu Python direktori paket apa (dan file Python yang dikandungnya) untuk disertakan.
 find_packages () menemukan direktori ini secara otomatis sehingga Anda tidak perlu mengetiknya. Untuk memasukkan file lain, seperti direktori statis dan template,
 include_package_data diatur. Python membutuhkan file lain bernama MANIFEST.in untuk memberi tahu apa data lain ini.

 Ini memberitahu Python untuk menyalin semuanya dalam direktori statis dan template, dan file schema.sql, tetapi untuk mengecualikan semua file bytecode.

Lihat panduan pengemasan resmi untuk penjelasan lain tentang file dan opsi yang digunakan.
Instal Proyek

Gunakan pip untuk menginstal proyek Anda di lingkungan virtual.

menginstal pip -e.

Ini memberitahu pip untuk menemukan setup.py di direktori saat ini dan menginstalnya dalam mode yang dapat diedit atau pengembangan.
Mode yang dapat diedit berarti bahwa ketika Anda membuat perubahan pada kode lokal Anda, Anda hanya perlu menginstal ulang jika Anda mengubah metadata tentang proyek, 
seperti dependensinya.

Anda dapat mengamati bahwa proyek sekarang diinstal dengan daftar pip.
Tidak ada perubahan dari cara Anda menjalankan proyek Anda sejauh ini. FLASK_APP masih diatur ke flaskr dan flask run masih menjalankan aplikasi.

Test Coverage

Tes riting unit untuk aplikasi Anda memungkinkan Anda memeriksa bahwa kode yang Anda tulis bekerja sesuai dengan yang Anda harapkan. 
Flask menyediakan klien uji yang mensimulasikan permintaan ke aplikasi dan mengembalikan data respons.

Anda harus menguji kode sebanyak mungkin. Kode dalam fungsi hanya berjalan ketika fungsi dipanggil, dan kode di cabang, seperti jika blok,
 hanya berjalan ketika kondisi terpenuhi. Anda ingin memastikan bahwa setiap fungsi diuji dengan data yang mencakup setiap cabang.

Semakin dekat Anda mendapatkan cakupan 100%, semakin nyaman Anda melakukan perubahan tidak terduga akan mengubah perilaku lainnya. Namun, 
cakupan 100% tidak menjamin bahwa aplikasi Anda tidak memiliki bug. Secara khusus,
 itu tidak menguji bagaimana pengguna berinteraksi dengan aplikasi di browser.
 Meskipun demikian, uji cakupan adalah alat penting untuk digunakan selama pengembangan.
 
 Catatan

Ini sedang diperkenalkan di akhir tutorial, tetapi dalam proyek masa depan Anda, Anda harus menguji saat Anda mengembangkan.

Anda akan menggunakan pytest dan cakupan untuk menguji dan mengukur kode Anda. Instal keduanya:

pip menginstal cakupan pytest

Pengaturan dan Jadwal

Kode pengujian terletak di direktori pengujian. Direktori ini berada di sebelah paket flaskr, bukan di dalamnya. 
File tes / conftest.py berisi fungsi pengaturan yang disebut perlengkapan yang setiap tes akan digunakan. 
Tes berada dalam modul Python yang dimulai dengan test_, dan setiap fungsi tes dalam modul tersebut juga dimulai dengan test_.

Setiap tes akan membuat file database sementara baru dan mengisi beberapa data yang akan digunakan dalam tes.
 Tulis file SQL untuk memasukkan data itu.
 
 Perlengkapan aplikasi akan memanggil pabrik dan meneruskan test_config
 untuk mengonfigurasi aplikasi dan database untuk pengujian daripada menggunakan konfigurasi pengembangan lokal Anda.
 
 tempfile.mkstemp () membuat dan membuka file sementara, mengembalikan objek file dan path ke sana. 
 Jalur DATABASE ditimpa sehingga menunjuk ke jalur sementara ini sebagai ganti folder instance. Setelah mengatur jalur,
 tabel basis data dibuat dan data uji dimasukkan. Setelah tes selesai, file sementara ditutup dan dihapus.

PENGUJIAN memberitahu Flask bahwa aplikasi sedang dalam mode uji coba.
 Flask mengubah beberapa perilaku internal sehingga lebih mudah untuk diuji, dan ekstensi lain juga dapat menggunakan bendera untuk memudahkan pengujian.

Perlengkapan klien memanggil app.test_client () dengan objek aplikasi yang dibuat oleh perlengkapan aplikasi. 
Tes akan menggunakan klien untuk membuat permintaan ke aplikasi tanpa menjalankan server.

Perlengkapan pelari mirip dengan klien. app.test_cli_runner () membuat pelari yang dapat memanggil perintah Klik terdaftar dengan aplikasi.

Pytest menggunakan perlengkapan dengan mencocokkan nama fungsi mereka dengan nama-nama argumen dalam fungsi tes.
 Misalnya, fungsi test_hello yang akan Anda tulis berikutnya membutuhkan argumen klien.
 Pytest mencocokkan dengan fungsi fixture klien, memanggilnya, dan meneruskan nilai yang dikembalikan ke fungsi tes.
 
 Factory
 
 Tidak banyak yang bisa dicoba tentang pabrik itu sendiri. Sebagian besar kode akan dieksekusi untuk setiap tes, jadi jika ada yang gagal, tes lain akan diperhatikan.

Satu-satunya perilaku yang dapat berubah adalah melewati konfigurasi uji. Jika konfigurasi tidak dilewatkan,
 harus ada konfigurasi default, jika tidak konfigurasi harus ditimpa.
 
 Database
 
 Dalam konteks aplikasi, get_db harus mengembalikan koneksi yang sama setiap kali dipanggil. Setelah konteksnya, koneksi harus ditutup.
 
 Authentication
 
 Untuk sebagian besar tampilan, pengguna harus masuk. Cara termudah untuk melakukan ini dalam pengujian adalah dengan membuat permintaan POST ke tampilan masuk dengan klien.
 Daripada menulisnya setiap waktu,
 Anda dapat menulis kelas dengan metode untuk melakukan itu, dan menggunakan perlengkapan untuk memberikannya kepada klien untuk setiap tes.
 
 Dengan fixture auth, Anda dapat memanggil auth.login () dalam tes untuk login sebagai pengguna tes, yang dimasukkan sebagai bagian dari data tes di perlengkapan aplikasi.

Tampilan daftar harus berhasil di GET. Pada POST dengan data formulir yang valid, ini harus dialihkan ke URL masuk dan data pengguna harus berada dalam basis data.
 Data yang tidak valid harus menampilkan pesan kesalahan.
 
 client.get () membuat permintaan GET dan mengembalikan objek Response yang dikembalikan oleh Flask. Demikian pula, client.post () membuat permintaan POST, mengubah data dict menjadi data form.

Untuk menguji apakah halaman berhasil dirender, permintaan sederhana dibuat dan diperiksa untuk status status2 OK 200. Jika rendering gagal, Flask akan mengembalikan kode Error Server Internal 500.

header akan memiliki header Lokasi dengan URL masuk ketika tampilan daftar beralih ke tampilan masuk.

data berisi tubuh respons sebagai byte. Jika Anda mengharapkan nilai tertentu untuk ditampilkan di halaman, periksa apakah itu dalam data. Byte harus dibandingkan dengan byte. Jika Anda ingin membandingkan teks Unicode, gunakan get_data (as_text = True) sebagai gantinya.

pytest.mark.parametrize memberitahu Pytest untuk menjalankan fungsi pengujian yang sama dengan argumen berbeda. Anda menggunakannya di sini untuk menguji berbagai pesan input dan kesalahan yang tidak valid tanpa menulis kode yang sama tiga kali.

Tes untuk tampilan login sangat mirip dengan yang untuk mendaftar. Daripada menguji data dalam database, sesi harus memiliki set user_id setelah login.


Blog

All the blog views use the auth fixture you wrote earlier. Call auth.login() and subsequent requests from the client will be logged in as the test user.

The index view should display information about the post that was added with the test data. When logged in as the author, there should be a link to edit the post.

You can also test some more authentication behavior while testing the index view. When not logged in, each page shows links to log in or register.
 When logged in, there’s a link to log out.
 
 Running the Tests
 
 Jika tes gagal, pytest akan menampilkan kesalahan yang muncul. Anda dapat menjalankan pytest -v untuk mendapatkan daftar dari setiap fungsi tes daripada titik-titik.

Untuk mengukur cakupan kode pengujian Anda, gunakan perintah cakupan untuk menjalankan pytest daripada menjalankannya secara langsung.

Deploy to Production

Bagian dari tutorial ini mengasumsikan Anda memiliki server yang ingin Anda terapkan aplikasi Anda. 
Ini memberikan ikhtisar tentang cara membuat file distribusi dan menginstalnya,
 tetapi tidak akan membahas secara spesifik tentang server atau perangkat lunak apa yang digunakan. 
 Anda dapat menyiapkan lingkungan baru di komputer pengembangan Anda untuk mencoba petunjuk di bawah ini,
 tetapi mungkin tidak boleh menggunakannya untuk hosting aplikasi publik nyata. Lihat Opsi Penerapan untuk daftar berbagai cara untuk menghosting aplikasi Anda.
 
 Build and Install
 
 Saat Anda ingin menerapkan aplikasi Anda di tempat lain, Anda membangun file distribusi. 
 Standar saat ini untuk distribusi Python adalah format roda, dengan ekstensi .whl. Pastikan perpustakaan roda diinstal terlebih dahulu:
 
 Configure the Secret Key
 Di awal tutorial Anda memberi nilai default untuk SECRET_KEY. Ini harus diubah menjadi beberapa byte acak dalam produksi. Jika tidak, p
 enyerang dapat menggunakan kunci 'dev' publik untuk memodifikasi cookie sesi, atau apa pun yang menggunakan kunci rahasia.
 
 Run with a Production Server
 When running publicly rather than in development, you should not use the built-in development server (flask run). 
 The development server is provided by Werkzeug for convenience, but is not designed to be particularly efficient, stable, or secure.

Instead, use a production WSGI server. For example, to use Waitress, first install it in the virtual environment:

Lihat Opsi Penerapan untuk daftar berbagai cara untuk menghosting aplikasi Anda. Pelayan hanyalah contoh, dipilih untuk tutorial karena mendukung Windows dan Linux.
 Ada banyak lagi opsi server dan penyebaran WSGI yang dapat Anda pilih untuk proyek Anda.
 
 Keep Developing
 
 Anda telah belajar tentang beberapa konsep Flask dan Python di seluruh tutorial. 
 Kembali dan tinjau tutorial dan bandingkan kode Anda dengan langkah-langkah yang Anda ambil untuk sampai ke sana. Bandingkan proyek Anda dengan proyek contoh,
 yang mungkin terlihat sedikit berbeda karena sifat langkah-demi-langkah dari tutorial.
 
 Ada lebih banyak untuk Flask daripada yang Anda lihat sejauh ini. Meski begitu, Anda sekarang sudah siap untuk mulai mengembangkan aplikasi web Anda sendiri. 
 Lihat Quickstart untuk ikhtisar tentang apa yang dapat dilakukan Flask, lalu selami dokumen untuk terus belajar. 
 Flask menggunakan Jinja, Klik, Werkzeug, dan ItsDangerous di belakang layar, dan mereka semua memiliki dokumentasi sendiri juga.
 Anda juga akan tertarik dengan Ekstensi yang membuat tugas seperti bekerja dengan database atau memvalidasi data formulir lebih mudah dan lebih kuat.
 
 Jika Anda ingin terus mengembangkan proyek Flaskr Anda, berikut beberapa ide untuk apa yang akan dicoba berikutnya:
 
 -Tampilan detail untuk menampilkan satu pos. Klik judul pos untuk membuka halamannya.
 -Suka / tidak seperti postingan.
 -Komentar
 -Tag. Mengklik tag menunjukkan semua posting dengan tag itu
 -Kotak pencarian yang menyaring halaman indeks berdasarkan nama.
 -Tampilan paged. Hanya menampilkan 5 posting per halaman
 -Unggah gambar untuk mengikuti postingan.
 -Format posting menggunakan Penurunan harga
 -Umpan RSS dari pos baru
 
 Bersenang-senanglah dan buat aplikasi luar biasa!