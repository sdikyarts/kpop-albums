from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponseRedirect
from main.forms import ArtistForm, AlbumForm
from .models import Artist, Album
from django.urls import reverse
from django.core import serializers


# DELETED THE ALBUM OF THE DAY SECTION

# Helper function to convert date strings to 'YYYY-MM-DD' format
def convert_date_string(date_string):
    return datetime.strptime(date_string, '%B %d, %Y').strftime('%Y-%m-%d')

def show_main(request):
    data = {
        'nama': 'Yasmine Putri Viryadhani',
        'npm': '2206081862',
        'kelas': 'PBP A',
        'nama_app': 'kpop-albums',
    }

    template_name = 'main.html'

    artists = Artist.objects.all().order_by('name')

    artist_data_list = []  # Initialize an empty list to store artist data

    for artist in artists:
        artist_data = {
            'name': artist.name,
            'artist_logo_url': artist.artist_logo.url,
            'albums_count': Album.objects.filter(artist=artist).count(),
            # Add other artist data as needed
        }
        artist_data_list.append(artist_data)

    return render(request, template_name, {'data': data, 'artists': artist_data_list})


# Function for artists' pages
def show_artist_detail(request, artist_name):
    artist_data = Artist.objects.get(name=artist_name)
    artist_data.former_members = artist_data.former_members.split(',') if artist_data.former_members else []
    artist_data.members = artist_data.members.split(',') if artist_data.members else []
    artist_data.sub_units = artist_data.sub_units.split(',') if artist_data.sub_units else []
    artist_data.supporters = artist_data.supporters.split(',') if artist_data.supporters else []

    # Retrieve the albums associated with the artist
    artist_albums = Album.objects.filter(artist=artist_data)

    template_name = 'artists.html'

    return render(request, template_name, {'artist_data': artist_data, 'artist_albums': artist_albums})


# Function for albums' pages
def show_album_detail(request, artist_name, album_name):
    # Retrieve the album data
    album_data = Album.objects.get(artist__name=artist_name, name=album_name)
    album_data.tracklist = album_data.tracklist.split(',') if album_data.tracklist else []

    # Retrieve the associated artist data
    artist_data = Artist.objects.get(name=artist_name)

    template_name = 'albums.html'

    return render(request, template_name, {'album_data': album_data, 'artist_data': artist_data, 'artist_name': artist_name})


# Function to show the full list of artists
def show_full_list(request):
    # Retrieve all artists from the Artist model
    artists = Artist.objects.all().order_by('name')

    template_name = 'full_list.html'

    # Pass the list of artists to the template without removing duplicates
    return render(request, template_name, {'artists': artists})

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

def add_album(request, artist_name):
    artist = Artist.objects.get(name=artist_name)

    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)

        if form.is_valid():
            album = form.save(commit=False)
            album.artist = artist  # Associate the album with the artist
            album.company = artist.company  # Set the album's company to be the same as the artist's company
            album.save()
            return HttpResponseRedirect(reverse('main:artist_detail', args=[artist_name]))
    else:
        # Pass the artist name and company as context to the template
        form = AlbumForm(initial={'artist': artist, 'company': artist.company})

    return render(request, 'add_album.html', {'form': form, 'artist': artist, 'artist_name': artist_name})

def reset_form(request):
    # Delete all form submissions (adjust this logic based on your needs)
    Artist.objects.all().delete()
    Album.objects.all().delete()

    # Redirect back to the main page or any other page you prefer
    return redirect('main:show_main') 

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
