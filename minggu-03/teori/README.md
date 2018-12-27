# Tutorial - bab 5
Struktur Data

Struktur Data
Struktur Data adalah struktur yang dapat menyimpan dan mengorganisasikan kumpulan data. Berikut struktur data yang ada dalam Python.

List
List adalah struktur data yang menyimpan koleksi data terurut, anda dapat menyimpan sequence / rangkaian item menggunakan list.

Item dalam list ditutup menggunakan kurung siku [] (list literal). Setelah list dibuat anda bisa menambah, 
mengurangi, dan mencari item pada list. Karena kita dapat menambah dan mengurangi item, list bersifat mutable.

Pengenalan singkat obyek dan class
List adalah contoh penggunaan obyek dan class. Ketika kita menggunakan variabel i dan mengisinya dengan nilai integer 5, 
sama dengan kita membuat obyek (instance) i dari class (tipe) int. Anda dapat membaca help(int) untuk membaca dokumentasi class integer.

Class mempunyai method, fungsi yang didefinisikan dalam class. Anda bisa menggunakan method ini pada obyek class tersebut. 
Sebagai contoh, Python menyediakan method append untuk class list. contoh_list.append('item 1') akan menambahkan string 'item 1' 
kedalam list contoh_list. Perhatikan notasi titik untuk mengakses method pada obyek.

Class juga mempunyai field yang sama halnya variabel yang digunakan hanya untuk class. Anda bisa menggunakan variabel / nama ini pada obyek class tersebut.

Tuple
Tuple mirip dengan list namun tuple bersifat immutable (tidak bisa diubah setelah didefinisikan).

Tuple dibuat dengan menspesifikasikan item tuple dipisahkan menggunakan tanda koma dan opsional diapit dengan tanda kurung.

Dictionary
Dictionary seperti buku alamat, dengan buku alamat anda bisa mencari alamat atau detail kontak hanya menggunakan nama orang yang anda cari. 
Kita mengasosiasikan key (nama) dengan value (detail). Catatan key harus bersifat unik, anda tidak bisa menemukan informasi yang tepat 
jika ada dua orang yang mempunyai nama yang sama dalam buku alamat anda.

Anda hanya bisa menggunakan obyek immutable (seperti string) untuk key/ kunci dictionary. Anda bisa menggunakan obyek mutable atau immutable untuk value dalam dictionary.

Dictionary dispesifikasikan menggunakan pasangan key dan value diapit menggunakan kurung kurawal, {key1: value1, key2: value2}.

Sequence
List, tuple dan string adalah contoh dari sequence. Kita dapat melakukan tes keanggotaan, operasi index(akses, slicing), dan iterasi pada sequence.

Set
Set adalah koleksi obyek yang tidak terurut. Digunakan ketika keberadaan obyek pada koleksi lebih penting daripada urutan dan berapa kali obyek muncul pada koleksi.

Referensi
Jika anda membuat obyek dan mengisinya ke variabel, variabel hanya me refer ke obyek dan tidak merepresentasikan obyek itu sendiri. 
Nama variabel menunjuk ke bagian memori komputer dimana obyek disimpan. Hal ini dinamakan binding antara nama ke obyek.

String
Tipe atau class String mempunyai method-method untuk memudahkan operasi string.