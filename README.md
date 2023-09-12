# Identitas
Nama                : Yasmine Putri Viryadhani<br>
NPM                 : 2206081862<br>
Kelas               : PBP A<br>
Nama App            : K-Pop Albums<br>
Link App Adaptable  :


<p>
<details>
<summary><h1>Checklist Tugas</h1></summary>

<!-- Markdown content here -->
<p>
<details>
<summary><h2>Membuat sebuah proyek Django baru<h2></summary>

<!-- Markdown content here -->
### Inisiasi Direktori Lokal
- Sebelum membuat proyek Django, dibuatlah sebuah direktori kosong baru di lokal. Saya menamainya sebagai <code>kpop_albums</code>
- Setelah membuat direktori, kita harus menginisiasi repositori Git kosong di direktori tersebut dengan perintah <code>git_init</code>
- Lalu, kita harus mengkonfigurasi username dan email GitHub ke repositori Git tersebut di Terminal (MacOS) dengan cara:
    ```
    git config user.name "<NAME>"
    git config user.email "<EMAIL>"
    ```
- Kita juga bisa mengkonfigurasi secara global dengan cara:<br>
    ```
    git config --global user.name "<NAME>"
    git config --global user.email
    ```
- Verifikasi git lokal dengan menginput kode <code>git config --list --local</code>

### Membuat repository baru di GitHub


### Instalasi + Inisiasi Django pada repository
- Menambahkan virtual environment ke dalam directory <code>kpop_albums</code> dengan menjalankan kode <code>python3 -m venv env</code> (di MacOS)
- Menjalankan virtual environment dengan cara <code>source env/bin/activate</code> (MacOS)
- Menyiapkan Dependencies dengan membuat berkas <code>requirements.txt</code> di directory yang sama, lalu menambahkan kode di bawah ke dalam berkas <code>.txt</code> tersebut:<br>
    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3                   
    ```
- Install dependencies dengan menjalankan <code>pip install -r requirements.txt</code>
- Buat proyek Django dengan nama <code>kpop_albums</code> dengan menjalankan perintah <code>django-admin startproject kpop_albums .</code>
- Tambahkan <code>*</code> pada <code>ALLOWED_HOSTS</code> di <code>settings.py</code><br>
    ```
    ...
    ALLOWED_HOSTS = ["*"]
    ...
    ```
- Setelah memastikan file <code>manage.py</code> ada di directory, jalankan instruksi <code>./manage.py runserver</code> (MacOS). Saat menjalankan domain http://localhost:8000 muncul animasi roket

### Push ke repository GitHub
- Buat file <code>.gitignore</code> (masih di directory <code>kpop_albums</code> yng luar), lalu isi dengan kode berikut <br>
    ```
    # Django
    *.log
    *.pot
    *.pyc
    __pycache__
    db.sqlite3
    media

    # Backup files
    *.bak 

    # If you are using PyCharm
    # User-specific stuff
    .idea/**/workspace.xml
    .idea/**/tasks.xml
    .idea/**/usage.statistics.xml
    .idea/**/dictionaries
    .idea/**/shelf

    # AWS User-specific
    .idea/**/aws.xml

    # Generated files
    .idea/**/contentModel.xml

    # Sensitive or high-churn files
    .idea/**/dataSources/
    .idea/**/dataSources.ids
    .idea/**/dataSources.local.xml
    .idea/**/sqlDataSources.xml
    .idea/**/dynamic.xml
    .idea/**/uiDesigner.xml
    .idea/**/dbnavigator.xml

    # Gradle
    .idea/**/gradle.xml
    .idea/**/libraries

    # File-based project format
    *.iws

    # IntelliJ
    out/

    # JIRA plugin
    atlassian-ide-plugin.xml

    # Python
    *.py[cod] 
    *$py.class 

    # Distribution / packaging 
    .Python build/ 
    develop-eggs/ 
    dist/ 
    downloads/ 
    eggs/ 
    .eggs/ 
    lib/ 
    lib64/ 
    parts/ 
    sdist/ 
    var/ 
    wheels/ 
    *.egg-info/ 
    .installed.cfg 
    *.egg 
    *.manifest 
    *.spec 

    # Installer logs 
    pip-log.txt 
    pip-delete-this-directory.txt 

    # Unit test / coverage reports 
    htmlcov/ 
    .tox/ 
    .coverage 
    .coverage.* 
    .cache 
    .pytest_cache/ 
    nosetests.xml 
    coverage.xml 
    *.cover 
    .hypothesis/ 

    # Jupyter Notebook 
    .ipynb_checkpoints 

    # pyenv 
    .python-version 

    # celery 
    celerybeat-schedule.* 

    # SageMath parsed files 
    *.sage.py 

    # Environments 
    .env 
    .venv 
    env/ 
    venv/ 
    ENV/ 
    env.bak/ 
    venv.bak/ 

    # mkdocs documentation 
    /site 

    # mypy 
    .mypy_cache/ 

    # Sublime Text
    *.tmlanguage.cache 
    *.tmPreferences.cache 
    *.stTheme.cache 
    *.sublime-workspace 
    *.sublime-project 

    # sftp configuration file 
    sftp-config.json 

    # Package control specific files Package 
    Control.last-run 
    Control.ca-list 
    Control.ca-bundle 
    Control.system-ca-bundle 
    GitHub.sublime-settings 

    # Visual Studio Code
    .vscode/* 
    !.vscode/settings.json 
    !.vscode/tasks.json 
    !.vscode/launch.json 
    !.vscode/extensions.json 
    .history
    ```
- Lakukan add, commit, dan push dari directory <code>kpop_albums</code> ke branch <code>main</code> di repository GitHub <code>kpop_albums</code> (ini akan mem-push README.md, proyek Django, dan .gitignore ke repository)<br>
    ```
    git add .
    git commit -m "Push README + .gitignore + proyek"
    git branch -M main
    git remote add origin "https://github.com/sdikyarts/kpop-albums.git"
    git push -u origin main
    ```
- Pastikan struktur direktori lokal dan repository GitHub sudah benar

</details>
</p>

<p>
<details>
<summary><h2>Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat<h2></summary>

<!-- Markdown content here -->
- Login ke [Adaptable.io](https://adaptable.io/)
- Tekan tombol <code>New App</code> lalu pilih <code>Connect an Existing Repository</code>
- Hubungkan [Adaptable.io](https://adaptable.io/) dengan GitHub dan pilih <code>All Repositories</code> pada proses instalasi
- Pilih proyek <code>kpop_albums</code> sebagai basis aplikasi yang akan di-deploy
- Pilih branch <code>main</code>
- Pilih <code>Python App Template</code> sebagai template deployment
- Pilih <code>PostgreSQL</code> sebagai tipe database yang digunakan
- Sesuaikan versi Python dengan spek aplikasi (saya memakai versi 3.10). Trik: gunakan command <code>python3 --version</code> (MacOS)
- Pada bagian <code>Start Command</code>, masukkan perintah <code>python3 manage.py migrate && gunicorn shopping_list.wsgi</code> (MacOS)
- Masukkan nama aplikasi <code>kpop-albums</code> sebagai nama domain situs web aplikasi
- Centang bagian <code>HTTP Listener on PORT</code> dan klik <code>Deploy App</code> untuk mendeploy app

</details>
</p>



## Membuat aplikasi <code>main</code> dalam proyek tersebut

### Konfigurasi model dan implementasi model dasar
- Aktifkan virtual environment terlebih dahulu
- Buat aplikasi <code>main</code> di directory <code>kpop_albums</code> (yang luar/utama) dengan cara
    ```
    python3 manage.py startapp main
    ```
- Mendaftarkan aplikasi <code>main</code> ke dalam proyek
    - Buka berkas <code>settings.py</code>
    - Tambahkan <code>'main'</code> di variabel <code>INSTALLED_APPS</code><br>
    ```
    INSTALLED_APPS = [
        ...,
        'main',
        ...
    ]
    ```
## Membuat dan mengisi berkas <code>main.html</code>
- Buat direktori baru <code>templates</code> di dalam direktori <code>main</code>
- Di dalam direktori baru <code>templates</code>, buat berkas HTML baru berjudul <code>main.html</code>, lalu isi sesuai selera :D

## Membuat model pada aplikasi <code>main</code> dengan nama <code>Item</code>

### Wajib mengandung atribut-atribut berikut:
- <code>name</code> sebagai nama *item* dengan tipe <code>CharField</code>
- <code>amount</code> sebagai jumlah *item* dengan tipe <code>IntegerField</code>
- <code>description</code> sebagai deskripsi *item* dengan tipe <code>TextField</code>

### Mengubah berkas <code>models.py</code> pada aplikasi <code>main</code>, lalu membuat dan mengaplikasikan migrasi model
- Buka berkas <code>models.py</code> di dalam direktori aplikasi <code>main</code>, kemudian isi dengan kode berikut:
- Jalankan perintah berikut untuk membuat berkas migrasi yang berisi perubahan model yang belum diaplikasikan ke dalam basis data
    ```
    python3 manage.py makemigrations
    ```
- Jalankan perintah berikut untuk menerapkan migrasi ke dalam basis data lokal
    ```
    python3 manage.py migrate
    ```


</details>
</p>

