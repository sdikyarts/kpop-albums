from django.forms import ModelForm, FileInput
from .models import Artist, Album

from django.utils.html import format_html

from django import forms
from django.utils.safestring import mark_safe

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'company', 'debut_date', 'disband_date', 'members', 'former_members', 
                  'sub_units', 'supporters', 'description', 'artist_pic', 'artist_logo'] 
    
    # Custom method to display artist_pic as a link
    def artist_pic_display(self):
        artist_pic = self.instance.artist_pic
        if artist_pic:
            return format_html('<a href="{}" target="_blank">{}</a>', artist_pic, artist_pic)
        return ""
    
    # Custom method to display artist_logo as a link
    def artist_logo_display(self):
        artist_logo = self.instance.artist_logo
        if artist_logo:
            return format_html('<a href="{}" target="_blank">{}</a>', artist_logo, artist_logo)
        return ""
    
    # Add this method to make the "disband_date", "former_members" and "sub_units" fields optional
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['disband_date'].required = False
        self.fields['former_members'].required = False
        self.fields['sub_units'].required = False
        self.fields['supporters'].required = False
    
    name = forms.CharField(
        label='Artist Name',
        widget=forms.Textarea(attrs={'rows': 1}),
    )

    company = forms.CharField(
        label = 'Company',
        widget=forms.Textarea(attrs={'rows': 1}),
    )

    debut_date = forms.DateField(
        label = 'Debut Date',
        widget=forms.Textarea(attrs={'rows': 1}),
    )

    disband_date = forms.DateField(
        label = 'Disband Date',
        widget=forms.Textarea(attrs={'rows': 1}),
        help_text='*add if present'
    )

    members = forms.CharField(
        label ='Members',
        widget=forms.Textarea(attrs={'rows': 4}),
    )

    former_members = forms.CharField(
        label = 'Former Member(s)',
        widget=forms.Textarea(attrs={'rows': 4}),
        help_text='*add if present'
    )

    sub_units = forms.CharField(
        label = 'Sub-Unit(s)',
        widget=forms.Textarea(attrs={'rows': 4}),
        help_text='*add if present'
    )

    supporters = forms.CharField(
        label = 'Fan Club Name(s)',
        widget=forms.Textarea(attrs={'rows': 1}),
        help_text='*add if present'
    )

    artist_pic = forms.ImageField(widget=forms.FileInput(attrs={'accept': 'image/*'}), required=False, help_text='*upload image')
    artist_logo = forms.ImageField(widget=forms.FileInput(attrs={'accept': 'image/*'}), required=False, help_text='*upload image')

    

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'release_date', 'company', 'price', 'amount', 
                  'tracklist', 'album_cover']

    # Custom method to display album_cover as a link
    def album_cover_display(self):
        album_cover = self.instance.album_cover
        if album_cover:
            return format_html('<a href="{}" target="_blank">{}</a>', album_cover, album_cover)
        return ""
    
    name = forms.CharField(
        label = "Album Title",
        widget=forms.Textarea(attrs={'rows': 1}),
    )

    release_date = forms.DateField(
        label = 'Release Date',
        widget=forms.Textarea(attrs={'rows': 1}),
    )

    company = forms.CharField(
        label = 'Label',
        widget=forms.Textarea(attrs={'rows': 1}),
    )

    price = forms.CharField(
        label = 'Price (in IDR)',
        widget=forms.Textarea(attrs={'rows': 1}),
    )

    amount = forms.CharField(
        label = 'Amount',
        widget=forms.Textarea(attrs={'rows': 1}),
    )
    
    tracklist = forms.CharField(
        label = 'Tracklist',
        widget=forms.Textarea(attrs={'rows': 8}),
    )

    album_cover = forms.ImageField(widget=forms.FileInput(attrs={'accept': 'image/*'}), required=False)

# Class untuk modifikasi form Register
class RegisterForm(UserCreationForm):
    class Meta:
        model = User  # Make sure to import User from django.contrib.auth.models
        fields = ['username', 'password1', 'password2']

    username = forms.CharField(
        label = 'Username',
    )

    password1 = forms.CharField(
        label = 'Password',
    )

    password2 = forms.CharField(
        label = 'Confirm Password',
    )
