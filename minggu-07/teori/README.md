# Tutorial - bab 9
OOP di Python

Pemrograman berorientasi objek, atau OOP singkatnya, adalah paradigma pemrograman yang menyediakan 
sarana untuk menyusun program sehingga sifat dan perilaku digabungkan menjadi objek individual. 
Misalnya, objek bisa mewakili seseorang dengan nama properti, umur, alamat, dll, 
dengan perilaku seperti berjalan, berbicara, bernafas, dan berlari. Atau email dengan properti seperti daftar penerima, 
subjek, badan, dll., Dan perilaku seperti menambahkan lampiran dan pengiriman.
Dengan kata lain, pemrograman berorientasi obyek adalah sebuah pendekatan untuk pemodelan beton, 
hal-hal dunia nyata seperti mobil dan juga hubungan antara hal-hal seperti perusahaan dan karyawan, 
siswa dan guru, dll. Model OOP entitas dunia nyata sebagai objek perangkat lunak, 
yang memiliki beberapa data yang terkait dengannya dan bisa melakukan fungsi tertentu.
Paradigma pemrograman umum lainnya adalah pemrograman prosedural yang menyusun program seperti 
resep karena menyediakan seperangkat langkah, dalam bentuk fungsi dan blok kode, 
yang mengalir secara berurutan untuk menyelesaikan tugas. Mengambil kunci adalah objek berada di pusat paradigma pemrograman berorientasi objek, 
tidak hanya mewakili data, seperti dalam pemrograman prosedural, namun juga dalam keseluruhan struktur program.

class dengan Python
Berfokus pertama pada data, masing-masing benda atau benda merupakan turunan dari beberapa class. 
Struktur data primitif yang tersedia dengan Python, seperti angka, string, 
dan daftar dirancang untuk mewakili hal-hal sederhana seperti biaya sesuatu, nama sebuah puisi, 
dan warna favorit Anda masing-masing.

class Dog: 
        pass

Objek Python (Contoh)
Sementara class adalah cetak biru, sebuah contoh adalah salinan class dengan nilai sebenarnya , 
secara harfiah merupakan objek milik class tertentu. Ini bukan ide lagi; Ini adalah hewan yang sebenarnya, 
seperti seekor Dog bernama Roger yang berusia delapan tahun.

class Dog(object):
    pass
	
Atribut Instance
Semua class membuat objek, dan semua objek mengandung karakteristik yang disebut atribut 
disebut sebagai properti pada paragraf pembuka). Gunakan __init__()metode untuk menginisialisasi 
(misalnya, tentukan) atribut awal objek dengan memberi mereka nilai default (atau side state). 
Metode ini harus memiliki setidaknya satu argumen dan juga selfvariabel, yang mengacu pada objek itu sendiri (misalnya, Dog).

Atribut class
Sementara atribut instance spesifik untuk setiap objek, atribut class sama untuk semua contoh — yang dalam hal ini adalah semua Dog.

Instantiating Objek
Instansiasi adalah istilah bagus untuk menciptakan instance class baru yang unik.

Sebagai contoh:

>>> class Dog:
...     pass
...
>>> Dog()
<__main__.Dog object at 0x1004ccc50>
>>> Dog()
<__main__.Dog object at 0x1004ccc90>
>>> a = Dog()
>>> b = Dog()
>>> a == b
False

Instance Methods
Metode Instance didefinisikan di dalam class dan digunakan untuk mendapatkan isi sebuah instance. 
Mereka juga bisa digunakan untuk melakukan operasi dengan atribut objek kita. Seperti __init__metodenya, argumen pertama selalu self:

class Dog:
# class Attribute
    species = 'mammal'
# Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
# instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)
# instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
# Instantiate the Dog object
mikey = Dog("Mikey", 6)
# call our instance methods
print(mikey.description())
print(mikey.speak("Gruff Gruff"))

Obyek Warisan Python
Warisan adalah proses dimana satu class mengambil atribut dan metode yang lain. 
class yang baru terbentuk disebut class anak , dan class class anak diturunkan dari class orang tua disebut .



