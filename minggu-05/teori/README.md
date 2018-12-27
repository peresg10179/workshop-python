# Tutorial - bab 7 
I/O

Print
Cara termudah untuk menghasilkan output adalah dengan menggunakan pernyataan cetak di mana 
Anda bisa melewati nol atau lebih banyak ekspresi yang dipisahkan dengan koma. 
Fungsi ini mengubah ekspresi yang Anda berikan ke string dan menulis hasilnya ke output standar sebagai berikut :

print ("Python adalah bahasa pemrograman yang hebat")

Membaca Input Keyboard
Python 2 memiliki dua fungsi built-in untuk membaca data dari input standar, 
yang secara default berasal dari keyboard. Fungsi ini adalah input() dan raw_input()

Dengan Python 3, fungsi raw_input() tidak digunakan lagi. Selain itu, input() berfungsi membaca data dari keyboard sebagai string, 
terlepas dari apakah itu tertutup dengan tanda kutip (‘’ atau ‘”) atau tidak.

Fungsi Input Python
Fungsi input([prompt]) setara dengan raw_input, kecuali mengasumsikan bahwa input adalah ekspresi Python yang valid dan mengembalikan hasil yang dievaluasi ke Anda.