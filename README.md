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
- Grup-grup yang saya gunakan sebagai contoh untuk membangun proyek ini adalah [**NCT**](https://en.m.wikipedia.org/wiki/NCT_(group)) dan [**Stray Kids**](https://en.wikipedia.org/wiki/Stray_Kids)
    - Karena keterbatasan waktu dalam *development* proyek ini, grup-grup lain akan ditambahkan seiring waktu

## Tampilan App (sementara)
- Progres **Tugas 2**
    <details>
    <summary>Show Images</summary>

    <img src="main view.png">
    </details>
- Progres **Tugas 3**
<img src="update tugas 3.png">


# Checklist Tugas 3
## ✅ Membuat input form untuk menambahkan objek model pada app sebelumnya.

### 1. Routing dari <code>main/</code> ke <code>/</code>
- Setelah menyalakan Virtual Environment dengan command <code>source env/bin/activate</code> (MacOS), saya memodifikasi <code>urls.py</code> yang ada di *root directory* <code>kpop_albums</code> dengan mengubah path <code>main</code> menjadi <code>''</code> pada bagian <code>urlpatterns</code>
<br>
    <img src="routing main.png">


### 2. Implementasi Skeleton sebagai Kerangka dari Views
- Pada *root directory* <code>kpop_albums</code>, saya membuat folder baru bernama <code>templates</code>. 
- Lalu didalamnya, saya membuat berkas <code>base.html</code> yang berisi kerangka untuk file-file HTML yang ada
    - Isi <code>base.html</code> yang saya buat dapat dilihat di [sini]()
- Di <code>settings.py</code> yang ada di *sub-directory* <code>kpop_albums</code>, saya memodifikasi bagian <code>TEMPLATES</code> seperti yang ada di kode spoiler di bawah:
    ```
    ...
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'], # Yang saya tambahkan ini
            'APP_DIRS': True,
            ...
        }
    ]
    ...
    ```

- Di *page-page* HTML yang ada di *directory* <code>templates</code> yang ada di *sub-directory* <code>main</code>, saya memodifikasi struktur masing-masing *page* dengan struktur yang ada di kode spoiler di bawah:
    <details>
    <summary>Show Code</summary>

    ```
    ...
    {% extends 'base.html' %}

    {% block meta %}
        # Isi dengan apapun yang sebelumnya ada di <head>
        # Umumnya berisi syntax <title>
    {% endblock meta %}

    {% block content %}
        # Isi dengan apapun yang sebelumnya ada di <body>
    {% endblock content %}
    ```
    </details>

### 3. Membuat Form Input Data
- Untuk efisiensi pengelolaan, saya mengganti model saya di <code>models.py</code> dari <code>Item</code> menjadi <code>Artist</code> dan <code>Album</code>
- Di *sub-directory* <code>main</code>, saya membuat file baru bernama <code>forms.py</code>
    - <code>forms.py</code> berfungsi untuk membuat struktur form yang dapat menerima data produk baru
    - Isi dari <code>forms.py</code> disesuaikan dengan *attributes* yang ada di <code>context</code> pada <code>forms.py</code>
    - Saya membuat dua forms, yaitu <code>ArtistForm</code> (untuk data artis) dan <code>AlbumForm</code> (untuk data album tiap artisnya)
    - Isi lengkap dari <code>forms.py</code> dapat dilihat di [sini]()
- Di <code>views.py</code>, saya menambahkan bebrapa import dan fungsi baru untuk menghasilkan formulir yang dapat menambahkan data artis dan album secara otomatis ketika data di-submit dari form.
    - Fungsi untuk menambahkan data artis dan album akan dijelaskan di section berikutnya
    - Saya juga menambahkan function <code>reset</code> untuk menghapus semua artis dan album mereka
        <details>
        <summary>Show Code</summary>

        ```
        def reset_form(request):
        # Delete all form submissions (adjust this logic based on your needs)
        Artist.objects.all().delete()
        Album.objects.all().delete()
        
        # Redirect back to the main page or any other page you prefer
        return redirect('main:show_main')
        ```
        </details>
    - Isi lengkap dari <code>views.py</code> dapat dilihat di [sini]()
- Lalu saya buat dua berkas HTML baru bernama <code>add_artist.html</code> dan <code>add_album.html</code> pada *directory* <code>main/templates</code>
    - Berikut isi lengkap dari:
        - [<code>add_artist.html</code>]()
        - [<code>add_album.html</code>]()

## ✅ Menambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID
### 1. Menampilkan Data Artis dan Album Pada HTML
- Terdapat dua fungsi menambah data artis dan album
    1. Fungsi <code>add_artist</code> untuk menambahkan artis melalui <code>ArtistForm</code>
        <details>
        <summary>Show Code</summary>

        ```
        def add_artist(request):
        if request.method == 'POST':
            form = ArtistForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                # Fetch all artists again after adding a new one
                artists = Artist.objects.all()
                return render(request, 'main.html', {'artists': artists})  # Pass the updated list of artists to the main page
        else:
            form = ArtistForm()

        context = {'form': form}
        return render(request, "add_artist.html", context)
        ```
        </details>
    2. Fungsi <code>add_album</code> untuk menambahkan artis melalui <code>AlbumForm</code> untuk masing-masing artis yang sudah terdaftar
        <details>
        <summary>Show Code</summary>

        ```
        def add_artist(request):
        if request.method == 'POST':
            form = ArtistForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                # Fetch all artists again after adding a new one
                artists = Artist.objects.all()
                return render(request, 'main.html', {'artists': artists})  # Pass the updated list of artists to the main page
        else:
            form = ArtistForm()

        context = {'form': form}
        return render(request, "add_artist.html", context)
        ```
        </details>
### 2. Menampilkan Data Produk Pada XML dan JSON
- Berikut potongan kode untuk XML dan JSON:
    <details>
    <summary>Show Code</summary>

    ```
    def show_xml(request):
        # Combine data from both Artist and Album models
        artist_data = Artist.objects.all()
        album_data = Album.objects.all()
        combined_data = list(artist_data) + list(album_data)

        # Serialize the combined data to XML format
        xml_data = serializers.serialize("xml", combined_data)

        return HttpResponse(xml_data, content_type="application/xml")

    def show_json(request):
        # Combine data from both Artist and Album models
        artist_data = Artist.objects.all()
        album_data = Album.objects.all()
        combined_data = list(artist_data) + list(album_data)

        # Serialize the combined data to JSON format
        json_data = serializers.serialize("json", combined_data)

        return HttpResponse(json_data, content_type="application/json")

    ```
    </details>
- Berikut potongan kode untuk XML dan JSON (by ID, hanya untuk Artis)
    <details>
    <summary>Show Code</summary>

    ```
    def show_xml_by_id(request, id):
        # Combine data from both Artist and Album models
        artist_data = Artist.objects.all().filter(pk=id)
        combined_data = list(artist_data)

        # Serialize the combined data to XML format
        xml_data = serializers.serialize("xml", combined_data)

        return HttpResponse(xml_data, content_type="application/xml")

    def show_json_by_id(request, id):
        # Combine data from both Artist and Album models
        artist_data = Artist.objects.all().filter(pk=id)
        combined_data = list(artist_data)

        # Serialize the combined data to JSON format
        json_data = serializers.serialize("json", combined_data)

        return HttpResponse(json_data, content_type="application/json")

    ```
    </details>
## ✅ Membuat routing URL untuk masing-masing views yang telah ditambahkan di poin 2
- Di <code>urls.py</code> pada *sub-directory* <code>main</code>, saya menambahkan import dan kode berikut untuk menambahkan path
    ```
    urlpatterns = [
        ...
        
        # tambahan baru
        path('add-artist', add_artist, name='add_artist'),
        path('add_album/<str:artist_name>/', add_album, name='add_album'),
        path('reset_form/', reset_form, name='reset_form'),
    ]
    ```
## Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman
HTML di Postman
<img src="html postman.png">

XML di Postman
<img src="xml postman.png">

JSON di Postman
<img src="json postman.png">

XML by ID di Postman
<img src="xml id.png">

JSON by ID di Postman
<img src="json id.png">

# Pertanyaan
### 1. Apa perbedaan antara form POST dan form GET dalam Django?
<details>
<summary>Show Answer</summary>

- Form POST digunakan untuk mengirim data ke server untuk mengupdate sebuah resource
- Form GET digunakan untuk me-request data dari sebuah source yang spesifik
</details>


### 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
<details>
<summary>Show Answer</summary>

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
</details>

### 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
<details>
<summary>Show Answer</summary>

- JSON sering digunakan dalam pertukaran data karena sifatnya yang *easy to read and write* serta kompatibel dengan berbagai bahasa pemrograman dan *framework*.
- JSON cocok digunakan untuk berbagai *web applications* karena ia menggunakan bahasa pemrograman JavaScript (biasa digunakan untuk *web app*) dan gampang di-*parse* oleh browser.
- Data yang direpresentasikan JSON berukuran lebih kecil dan lebih sedikit memakan biaya daripada XML.
- Idealnya digunakan saat kita ingin mengirim data yang simpel dan dinamis, contohnya user preferences, settings, atau analytics.
</details>


### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Baca bagian [Checklist Tugas 3](#checklist-tugas-3) di atas