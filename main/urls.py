from django.urls import path
from main.views import show_main, show_artist_detail, show_album_detail, show_full_list

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('artist/<str:artist_name>/', show_artist_detail, name='artist_detail'),
    path('album/<str:artist_name>/<str:album_name>/', show_album_detail, name='album_detail'),
    path('directory/', show_full_list, name='full_list'),
]

