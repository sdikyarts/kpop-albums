# Identitas
Nama                : Yasmine Putri Viryadhani
NPM                 : 2206081862
Kelas               : PBP A
Nama App            : K-Pop Albums
Link App Adaptable  :

# Checklist Tugas
## Membuat sebuah proyek Django baru
1. Inisiasi Direktori Lokal
    - Sebelum membuat proyek Django, dibuatlah sebuah direktori kosong baru di lokal. Saya menamainya sebagai <code>kpop_albums</code>
    - Setelah membuat direktori, kita harus menginisiasi repositori Git kosong di direktori tersebut dengan perintah <code>git_init</code>
    - Lalu, kita harus mengkonfigurasi username dan email GitHub ke repositori Git tersebut di Terminal (MacOS) dengan cara:
    ```
    <code>git config user.name "<NAME>"</code>
    <code>git config user.email "<EMAIL>"</code>
    ```
    - Kita juga bisa mengkonfigurasi secara global dengan cara:
    ```
    git config --global user.name "<NAME>"
    git config --global user.email
    ```
    - Verifikasi git lokal dengan menginput kode <code>git config --list --local</code>
2. Membuat repository baru di GitHub

3. Instalasi + Inisiasi Django pada repository
    - Menambahkan virtual environment ke dalam directory <code>kpop_albums</code> dengan menjalankan kode <code>python3 -m venv env</code> (di MacOS)
    - Menjalankan virtual environment dengan cara <code>source env/bin/activate</code> (MacOS)
    - Menyiapkan Dependencies dengan membuat berkas <code>requirements.txt</code> di directory yang sama, lalu menambahkan kode di bawah ke dalam berkas <code>.txt</code> tersebut:
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
    - Tambahkan <code>*</code> pada <code>ALLOWED_HOSTS</code> di <code>settings.py</code>
    ```
    ...
    ALLOWED_HOSTS = ["*"]
    ...
    ```
    - Setelah memastikan file <code>manage.py</code> ada di directory, jalankan instruksi <code>./manage.py runserver</code> (MacOS). Saat menjalankan domain http://localhost:8000 muncul animasi roket
4. Push ke repository GitHub
    - Buat file <code>.gitignore</code> (masih di directory <code>kpop_albums</code> yng luar), lalu isi dengan kode berikut:
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
    - Lakukan add, commit, dan push dari directory <code>kpop_albums</code> ke branch <code>main</code> di repository GitHub <code>kpop_albums</code> (ini akan mem-push README.md, proyek Django, dan .gitignore ke repository)
    ```
    git add .
    git commit -m "Push README + .gitignore + proyek"
    git branch -M main
    git remote add origin "https://github.com/sdikyarts/kpop-albums.git"
    git push -u origin main
    ```