from django.test import TestCase, Client
from main.models import Item
from main.views import get_artist_data
from datetime import datetime

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

# BONUS = Testing Item (gaada di tutorial)
class itemTest(TestCase):
    def test_item_have_all_attribute(self):
        # Get data from get_artist_data() function
        artist_data = get_artist_data()[0]  # Assuming you want to use data from the first artist

        # Helper function to convert date strings to "YYYY-MM-DD" format
        def convert_date_string(date_string):
            return datetime.strptime(date_string, '%B %d, %Y').strftime('%Y-%m-%d')

        # Create an Item object based on artist_data
        item = Item.objects.create(
            description=artist_data['description'],
            artist = artist_data['artist'],  # You can use artist's name here
            artist_logo = artist_data['artist_logo'],
            company = artist_data['company'],
            debut_date = convert_date_string(artist_data['debut_date']),
            disband_date = None,  # Set this to None or as needed
            members = ', '.join(artist_data['members']),  # Convert members list to a string
            former_members = ', '.join(artist_data['former_members']),  # Convert former_members list to a string
            sub_units = ', '.join(artist_data['sub_units']),  # Convert sub_units list to a string
            supporters = ', '.join(artist_data['supporters']),  # Convert supporters list to a string
            artist_pic = artist_data['artist_pic'],
        )

        # Assuming you want to create an Item for an album from artist_data['albums'][0]
        album_data = artist_data['albums'][0]

        # Update the Item attributes with album-specific details
        item.name = album_data['name']
        item.release_date = convert_date_string(album_data['release_date'])
        item.price = album_data['price']
        item.amount = album_data['amount']
        item.tracklist = ', '.join(album_data['tracklist'])
        item.album_cover = album_data['album_cover']
        item.save()

        # Add more assertions as needed to check the attributes of the created Item
        self.assertEqual(item.description, artist_data['description'])
        self.assertEqual(item.artist, artist_data['artist'])
        self.assertEqual(item.artist_logo, artist_data['artist_logo'])
        self.assertEqual(item.company, artist_data['company'])
        self.assertEqual(item.debut_date, convert_date_string(artist_data['debut_date']))
        self.assertEqual(item.members, ', '.join(artist_data['members']))
        self.assertEqual(item.former_members, ', '.join(artist_data['former_members']))
        self.assertEqual(item.sub_units, ', '.join(artist_data['sub_units']))
        self.assertEqual(item.supporters, ', '.join(artist_data['supporters']))
        self.assertEqual(item.artist_pic, artist_data['artist_pic'])

        # Assert album-specific attributes
        self.assertEqual(item.name, album_data['name'])
        self.assertEqual(item.release_date, convert_date_string(album_data['release_date']))
        self.assertEqual(item.price, album_data['price'])
        self.assertEqual(item.amount, album_data['amount'])
        self.assertEqual(item.tracklist, ', '.join(album_data['tracklist']))
        self.assertEqual(item.album_cover, album_data['album_cover'])