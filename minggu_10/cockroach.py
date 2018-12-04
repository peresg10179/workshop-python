Langkah 1. Instal driver psycopg2

Untuk menginstal driver Python psycopg2, jalankan perintah berikut
$ pip install psycopg2]

Langkah 2. Buat  roach max dan database  Mulai klien SQL built-in:
$ cockroach sql --certs-dir=certs

Di shell SQL, berikan pernyataan berikut untuk membuat basis data  dan bank maksimum:
> CREATE USER IF NOT EXISTS maxroach;
> CREATE DATABASE bank;

Berikan  maxroach izin yang diperlukan:
> GRANT ALL ON DATABASE bank TO maxroach;

keluar dari SQL shell:
> \q

Langkah 3. Hasilkan sertifikat untuk pengguna maxroach

Buat sertifikat dan kunci untuk pengguna maxroach dengan menjalankan perintah berikut. 
$ cockroach cert create-client maxroach --certs-dir=certs --ca-key=my-safe-directory/ca.key

Langkah 4. Jalankan kode Python

Sekarang Anda memiliki database dan pengguna, Anda akan menjalankan kode yang ditunjukkan di bawah ini untuk:

   * Buat tabel dan masukkan beberapa baris
    *Baca dan perbarui nilai sebagai transaksi atom

Pernyataan dasar

Pertama, gunakan kode berikut untuk terhubung sebagai pengguna maxroach dan jalankan beberapa pernyataan dasar SQL, membuat tabel, menyisipkan baris, dan membaca serta mencetak baris.
Unduh file basic-sample.py, atau buat file sendiri dan salin kode ke dalamnya.





Kemudian jalankan kode:
$ python basic-sample.py

Outputnya harus



Transaksi (dengan logika coba lagi)

Selanjutnya, gunakan kode berikut untuk menghubungkan lagi sebagai pengguna maxroach tetapi kali ini menjalankan kumpulan pernyataan sebagai transaksi atom untuk mentransfer dana dari satu akun ke akun lainnya, di mana semua pernyataan yang disertakan dilakukan atau dibatalkan.

Unduh file txn-sample.py, atau buat file sendiri dan salin kode ke dalamnya. Outputnya harus:


catatan:

CockroachDB mungkin meminta klien untuk mencoba kembali transaksi jika terjadi pertentangan baca / tulis. 
CockroachDB menyediakan fungsi retry generik yang berjalan di dalam transaksi dan mencoba lagi sesuai kebutuhan. 
Anda dapat menyalin dan menempelkan fungsi coba kembali dari sini ke kode Anda.



menjalanakan code:
$ python txn-sample.py

outputnya harus :
Balances after transfer:
['1', '900']
['2', '350']


Untuk memverifikasi bahwa dana ditransfer dari satu akun ke yang lain, mulai klien SQL built-in
$ cockroach sql --certs-dir=certs --database=bank
Untuk memeriksa saldo akun, berikan pernyataan berikut:
> SELECT id, balance FROM accounts;

