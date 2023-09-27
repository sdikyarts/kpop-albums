from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.forms import ArtistForm, AlbumForm
from .models import Artist, Album
from django.core import serializers

from django.shortcuts import redirect
from django.contrib import messages  

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required

import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import RegisterForm 

from django.http import JsonResponse

# DELETED THE ALBUM OF THE DAY SECTION

# Helper function to convert date strings to 'YYYY-MM-DD' format
def convert_date_string(date_string):
    return datetime.strptime(date_string, '%B %d, %Y').strftime('%Y-%m-%d')

@login_required(login_url='/login')
## TUGAS 2 ##
def show_main(request):

    template_name = 'main.html'

    artists = Artist.objects.all().filter(user=request.user).order_by('name')

    artist_data_list = []  # Initialize an empty list to store artist data

    data = {
        'name': request.user.username,
        'last_login': request.COOKIES['last_login']
    }

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
    artist_albums = Album.objects.filter(artist=artist_data).order_by('release_date')

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
    artists = Artist.objects.all().filter(user=request.user).order_by('name')

    template_name = 'full_list.html'

    # Pass the list of artists to the template without removing duplicates
    return render(request, template_name, {'artists': artists})

## TUGAS 3 ##
def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            artist = form.save(commit=False)
            artist.user = request.user  # Set the user field with the currently logged-in user
            artist.save()
            return HttpResponseRedirect(reverse('main:show_main'))
    else:
        form = ArtistForm()

    context = {'form': form}
    return render(request, "add_artist.html", context)

def add_album(request, artist_name):
    artist = Artist.objects.get(name=artist_name, user=request.user)  # Ensure the artist belongs to the current user

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

## TUGAS 4 ##
def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

# Bonus Tugas 4: Menambahkan fungsi update jumlah amount (tombol plus-minus)
def update_album_amount(request, album_id):
    # Get the album object by its ID
    album = Album.objects.get(pk=album_id)

    # Check if the request method is POST
    if request.method == 'POST':
        action = request.POST.get('action', None)

        # Update the album amount based on the action
        if action == 'plus':
            album.amount += 1
        elif action == 'minus':
            if album.amount > 0:
                album.amount -= 1

        # Save the updated album object
        album.save()

        return JsonResponse({'success': True, 'new_amount': album.amount})


# Bonus Tugas 4: Menghapus Artis dan Album dari Inventory
def delete_artist(request, artist_name):
    # Ensure the artist belongs to the current user and delete it
    artist = Artist.objects.filter(name=artist_name, user=request.user).first()
    if artist:
        # Delete albums associated with the artist
        Album.objects.filter(artist=artist).delete()
        artist.delete()
    return redirect('main:show_main')

def delete_album(request, artist_name, album_name):
    # Ensure the album belongs to the current user and delete it
    album = Album.objects.filter(artist__name=artist_name, name=album_name, artist__user=request.user).first()
    if album:
        album.delete()
    return redirect('main:artist_detail', artist_name=artist_name)