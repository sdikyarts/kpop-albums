from django.urls import path
from main.views import show_main, show_artist_detail, show_album_detail, show_full_list
from main.views import add_artist, add_album, reset_form
from main.views import show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('artist/<str:artist_name>/', show_artist_detail, name='artist_detail'),
    path('album/<str:artist_name>/<str:album_name>/', show_album_detail, name='album_detail'),
    path('directory/', show_full_list, name='full_list'),
    
    # tambahan baru
    path('add-artist', add_artist, name='add_artist'),
    path('add_album/<str:artist_name>/', add_album, name='add_album'),
    path('reset_form/', reset_form, name='reset_form'),

    # xml and json
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
]

