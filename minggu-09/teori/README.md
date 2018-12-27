# Tutorial - bab 12
Virtual Environment dan Package Manager

Virtualenv (Virtual Environment) berguna untuk membuat virtual environment dengan mudah tanpa 
mempengaruhi python di sistem operasi anda. Ingin tes apakah aplikasi anda 
berjalan di modules versi terbaru? gampang, tinggal buat virtualenv dengan
menggunakan modules versi terbaru, modules tersebut tidak akan terinstall
di python sistem operasi kita, lalu cek apakah aplikasi kita berjalan, 
jika tidak maka tinggal hapus saja virtualenv tersebut. 
virtualenv juga menyediakan kita memilih interpreter yang kita inginkan, 
misal python 2.7 maupun 3.4 dan juga apakah include modules yang sudah 
terinstall di python sistem operasi kita atau tidak. Catatan, 
kita juga harus meng-install terlebih dahulu versi python di komputer 
kita sebelum kita ingin membuat virtualenv dengan versi tersebut.

pip install virtualenv
Dengan menggunakan terminal, pindah ke folder yang and ingin virtualenv dibuat, 
lalu jalankan perintah berikut.

virtualenv aplikasiPOS
Nantinya akan terbuat folder dengan nama environment yang berisi versi 
intrepeter yang sama dengan yang anda gunakan dan juga tanpa modules apapun. 
Sama seperti fresh install python. Nah untuk mengaktifkan/menggunakan virtualenv 
tersebut kita menggunakan file bat yang berada di nama-virtualenv\Scripts\activate.bat

aplikasiPOS\Scripts\activate.bat
atau di linux

source aplikasiPOS\Scripts\activate

nantinya di terminal anda akan ada tulisan virtualenv yang sedang aktif, seperti

(aplikasiPOS) G:\virtualenv\
Setelah aktif, kita bisa gunakan pip untuk menginstall modules-modules yang kita 
butuhkan atau dengan menggunakan requirements.txt. Modules apapun yang anda install 
hanya akan ter-install di virtual environment aplikasiPOS, sehingga anda tidak perlu 
khawatir dengan python sistem operasi anda, atau mungkin anda ingin membuat beberapa 
aplikasi yang menggunakan modules yang sama namun versi modules yang berbeda, maka virtualenv akan sangat berguna.
  
untuk deactivate virtualenv yang sedang aktif, kita hanya ketik perintah

deactivate


untuk membuat virtualenv dengan versi python tertentu
virtualenv --python=c:\Python34\python.exe namavirtualenv

untuk membuat virtualenv menggunakan modules yang sudah terinstall pada python kita

virtualenv --system-site-packages namavirtualenv

Package Manager atau juga disebut pip adalah singkatan dari Pip Installs Python atau PIP Installs Packages, 
kepanjangannya tidak perlu diperhatikan karena memang kalau diartikan terdengar aneh. 
Bayangkan pip adalah sebuah app store (atau biasa disebut sebagai package manager), 
kita bisa mencari, menginstall, me-manage modules atau package pada installasi python kita. 
Berikut merupakan fungsi-fungsi dasar PIP.

1.Install modules
2.uninstall modules
3.search modules yang tersedia
4.mengecek versi modules dan modules apa saja yang terinstall

Walaupun fungsinya sederhana namun sangat memberikan kemudahan dibandingkan 
dengan cara menambahkan modules secara konvesional, 
dimana kita harus men-download source modules dengan mencarinya di internet, 
menambahkannya ke site-packages atau menjalankan script setup jika disediakan, 
dan juga jika modules sudah berjumlah banyak maka akan cukup merepotkan untuk 
keep on track modules-modules apa saja yang sudah kita install atau mengecek versinya. 
pip mengatasi semua masalah itu, untuk menginstall sebuah modules anda hanya 
cukup membuka command line dan mengetik commandnya. Berikut merupakan command-command dasar pada pip.

pip install <package name>

Contoh jika kita ingin meng-install django kita gunakan command "pip install django", 
maka akan pip akan otomatis me-download django versi terakhir dan beserta dependencies yang dibutuhkannya.

pip show <package name>
Digunakan untuk memberi informasi suatu package yang sudah terinstall. 
Informasi yang diberikan adalah versi, lokasi package, dan dependencies dari package tersebut.

pip list
Digunakan untuk melihat semua package yang sudah terinstall.

pip uninstall <package name>
self-explanatory.

Untuk melihat semua packages bisa dilihat di website PyPI (Python Packages Index). 
Anda juga bisa meng-install suatu package dengan versi tertentu dengan contoh command berikut

pip install django==1.6.0