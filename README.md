# Identitas
Nama                : Yasmine Putri Viryadhani<br>
NPM                 : 2206081862<br>
Kelas               : PBP A<br>
Nama App            : K-Pop Albums<br>
Link App            : 

# Penjelasan App
## Latar Belakang
- Tema besar aplikasi untuk tugas PBP adalah aplikasi pengelolaan (inventori)
- Tema yang saya pilih adalah <b>inventori album K-Pop</b>
- Banyaknya jumlah grup yang debut dan album yang dirilis sehingga memungkinkan untuk dilakukan pengorganisasian album berdasarkan artis yang merilis album tersebut

## Contoh Proyek
- Grup-grup yang saya gunakan sebagai contoh untuk membangun proyek ini adalah [<b>NCT</b>](https://en.m.wikipedia.org/wiki/NCT_(group)) dan [<b>Stray Kids</b>](https://en.wikipedia.org/wiki/Stray_Kids)
    - Karena keterbatasan waktu dalam *development* proyek ini, grup-grup lain akan ditambahkan seiring waktu

## Tampilan App (sementara)
<img src="main view.png">


# Checklist Tugas 3
## ✅ Membuat input form untuk menambahkan objek model pada app sebelumnya.

### 1. Routing dari <code>main/</code> ke <code>/</code>
- Setelah menyalakan Virtual Environment dengan command <code>source env/bin/activate</code> (MacOS), saya memodifikasi <code>urls.py</code> yang ada di *root directory* <code>kpop_albums</code> dengan mengubah path <code>main</code> menjadi <code>''</code> pada bagian <code>urlpatterns</code>
<br>
<img src="routing main.png">


### 2. Implementasi Skeleton sebagai Kerangka dari Views
- Pada *root directory* <code>kpop_albums</code>, saya membuat folder baru bernama <code>templates</code>. 
- Lalu didalamnya, saya membuat berkas <code>base.html</code>


# Pertanyaan
### 1. Apa perbedaan antara form POST dan form GET dalam Django?
- Form POST digunakan untuk mengirim data ke server untuk mengupdate sebuah resource
- Form GET digunakan untuk me-request data dari sebuah source yang spesifik


### 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
- XML 
    - Merupakan Extensible Markup Language, diturunkan dari SGMl
    - Merupakan markup language dan menggunakan Tag Structure untuk merepresentasikan *data items*
    - Lebih sulit untuk dibaca karena bahasanya yang kompleks
    - Merepresentasikan data dengan ukuran yang lebih besar dari JSON sehingga data lebih lambat ditransfer
- JSON
    - Merupakan JavaScript Object Notation yang dibuat berdasarkan bahasa pemrograman JavaScript
    - Merepresentasikan *data items* dalam bentuk objek
    - Tidak menggunakan Tag Structure, memungkinkan untuk lebih mudah dibaca
    - Merepresentasikan data dengan ukuran yang lebih kecil dari XML sehingga data lebih cepat ditransfer
- HTML
    - Merupakan, Hypertext Markup Language, salah satu website standar pada World Wide Web Consortium atau W3
    - Digunakan untuk mendeskripsikan bagaimana data akan di-display
    - Menjadi *primary building block* dari *sebuah web development*
    - Menjadi sarana untuk menentukan struktur web
    - XML dan JSON adalah bagian *raw data* yang ditampilkan HTML



### Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
- JSON sering digunakan dalam pertukaran data karena sifatnya yang *easy to read and write *serta kompatibel dengan berbagai bahasa pemrograman dan *framework*.
- JSON cocok digunakan untuk berbagai *web applications* karena ia menggunakan bahasa pemrograman JavaScript (biasa digunakan untuk *web app*) dan gampang di-*parse* oleh browser.
- Data yang direpresentasikan JSON berukuran lebih kecil dan lebih sedikit memakan biaya daripada XML.
- Idealnya digunakan saat kita ingin mengirim data yang simpel dan dinamis, contohnya user preferences, settings, atau analytics.


### 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
- Baca bagian [Checklist Tugas 3](#checklist-tugas-3) di atas