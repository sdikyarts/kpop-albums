from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from datetime import datetime

import random


# Helper function to convert date strings to 'YYYY-MM-DD' format
def convert_date_string(date_string):
    return datetime.strptime(date_string, '%B %d, %Y').strftime('%Y-%m-%d')


# Fungsi Context untuk menampung data artis
def get_artist_data():
    return [
        {
            'artist': 'Stray Kids',
            'company': 'JYP Entertainment',
            'debut_date': 'March 25, 2018',

            'members': ['Bang Chan', 'Lee Know', 'Changbin', 'Hyunjin',
                        'Han', 'Felix', 'Seungmin', 'I.N'],
            'former_members': ['Woojin'],

            'sub_units': ['3RACHA'],

            'supporters': ['Stay'],

            'description': 'Being a fully self-produced boy group with 8 members, Stray Kids is a South Korean boy group formed by JYP Entertainment in 2018 from the 2017 reality show of the same name.',

            # Albums: Only took 3 full albums sebagai contoh
            'albums': [
                {
                    'name': 'GO生',
                    'release_date': 'June 17, 2020',
                    'amount': '1',
                    'price': '300000',
                    'tracklist': [
                        'GO生', '神메뉴 (God\'s Menu)', 'Easy', 'Pacemaker',
                        '비행기 (Airplane)', '일상 (Another Day)', 'Phobia',
                        '청사진 (Blueprint)', '타 (TA)', 'Haven', 'TOP (\"신의 탑\" OST)',
                        'SLUMP (\"신의 탑\" OST)', 'Mixtape: Gone Days',
                        'Mixtape: 바보라도 알아 (On Track)'
                    ],
                    'album_cover': 'https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/51/d8/58/51d858b1-94df-2047-d2b4-0378ca0cd9db/192641939440_Cover.jpg/1000x1000bb.jpg'
                },
                {
                    'name': 'NOEASY',
                    'release_date': 'August 23, 2021',
                    'amount': '2',
                    'price': '350000',
                    'tracklist': [
                        'CHEESE', '소리꾼 (Thunderous)', 'DOMINO', '씩 (SSICK)',
                        'The View', '좋아해서 미안 (Sorry, I Love You)', 'Silent Cry',
                        '말할 수 없는 비밀 (Secret Secret)',
                        'Star Lost', '강박 (Red Lights)', 'Surfin\'', 'Gone Away',
                        'WOLFGANG', 'Mixtape: 애 (OH)'
                    ],
                    'album_cover': 'https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/af/dc/2b/afdc2b64-deb3-cf5f-84e2-c43be4105636/192641939495_Cover.jpg/1000x1000bb.jpg'
                },
                {
                    'name': '5-STAR',
                    'release_date': 'June 2, 2023',
                    'amount': '3',
                    'price': '400000',
                    'tracklist': [
                        '위인전 (Hall of Fame)', 'ITEM', 'Super Bowl', 'TOPLINE (feat. Tiger JK)',
                        'DLC', '죽어보자 (GET LIT)', '충돌 (Collision)', 'FNF', 'Youtiful',
                        'THE SOUND (Korean Ver.)', 'Mixtape: Time Out'
                    ],
                    'album_cover': 'https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/5a/3b/1e/5a3b1e2f-1b70-a4b0-6d4d-a33a770f361f/738676860696_Cover.jpg/1000x1000bb.jpg'
                }
            ],
            'artist_pic': 'https://cdn.antaranews.com/cache/1200x800/2022/09/07/FaH2ph5UEAA2sn8.jpeg',
            'artist_logo': 'https://i.pinimg.com/originals/81/f4/1b/81f41bea62ee391bd41d6e72cd0e8424.jpg'
        },
        {
            'artist': 'NCT',
            'company': 'SM Entertainment',
            'debut_date': 'April 9, 2016',

            'members': ['Taeil', 'Johnny', 'Taeyong', 'Yuta', 'Kun', 'Doyoung', 'Ten', 'Jaehyun',
                        'Winwin', 'Jungwoo', 'Mark', 'Xiaojun', 'Hendery', 'Renjun', 'Jeno',
                        'Haechan', 'Jaemin', 'Yangyang', 'Chenle', 'Jisung'],
            'former_members': ['Lucas', 'Shotaro', 'Sungchan'],

            'sub_units': ['NCT U', 'NCT 127', 'NCT Dream', 'WayV', 'NCT DOJAEJUNG', 'NCT Tokyo'],

            'supporters': ['NCTzen', 'WayZenNi (WayV only)'],

            'description': 'Currently the largest Korean boy group with 20 members, NCT is a South Korean group formed by SM Entertainment in 2016 which used to implement the unlimited members system.',

            # Albums: Only took 4 full albums
            'albums': [
                {
                    'name': 'NCT 2018 EMPATHY',
                    'release_date': 'March 14, 2018',
                    'amount': '1',
                    'price': '240000',
                    'tracklist': [
                        'INTRO: Neo Got My Back', 'BOSS', 'Baby Don\'t Stop', 'GO',
                        'TOUCH', 'YESTODAY', 'Black on Black', '텐데... (Timeless)',
                        '일곱 번째 감각 (第七感 ; The 7th Sense)', 'WITHOUT YOU',
                        'WITHOUT YOU (Chinese Ver.)', '夢中夢 (몽중몽); Dream In A Dream',
                        'OUTRO: VISION', 'YESTODAY (Extended Ver.)'
                    ],
                    'album_cover': 'https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/4b/3c/67/4b3c67ba-2721-19ce-424d-6742f420e800/NCT2018_EMPATHY_COVER_4000x4000px_1.jpg/1000x1000bb.jpg'
                },
                {
                    'name': 'NCT 2020 RESONANCE Pt. 1',
                    'release_date': 'October 12, 2020',
                    'amount': '2',
                    'price': '300000',
                    'tracklist': [
                        'Make A Wish (Birthday Song)', 'Misfit', 'Volcano', '백열등 (Light Bulb)',
                        'Dancing In The Rain', 'Interlude: Past to Present', '무대로 (Déjà Vu;舞代路)',
                        '月之迷 (Nectar)', 'Music, Dance', '피아노 (Faded In My Last Song)',
                        'From Home', 'From Home (Korean Ver.)', 'Make A Wish (Birthday Song) (English Ver.)'
                    ],
                    'album_cover': 'https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/c5/6e/65/c56e6560-19a8-51f3-347b-3b63068c53e6/NCT_RESONANCE_pt1_F.jpg/1000x1000bb.jpg'
                },
                {
                    'name': 'Universe',
                    'release_date': 'December 14, 2021',
                    'amount': '3',
                    'price': '360000',
                    'tracklist': [
                        'New Axis', 'Universe (Let\'s Play Ball)', 'Earthquake', 'OK!', 'Birthday Party',
                        'Know Now', 'Dreaming', 'Round&Round', 'Miracle', 'Vroom', 'Sweet Dream',
                        '별자리 (Good Night)', 'Beautiful'
                    ],
                    'album_cover': 'https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/e6/a0/68/e6a0689a-8d8d-4129-3319-cd02469eb48d/KakaoTalk_Photo_2021-11-29-12-29-12.jpg/1000x1000bb.jpg'
                },
                {
                    'name': 'Golden Age',
                    'release_date': 'August 28, 2023',
                    'amount': '4',
                    'price': '420000',
                    'tracklist': [
                        'Baggy Jeans', 'Call D', 'PADO', 'Interlude: Oasis', 'The BAT',
                        'Alley Oop', 'Tha\'s Not Fair', 'Kangaroo', 'Not Your Fault', 'Golden Age'
                    ],
                    'album_cover': 'https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/8e/b1/68/8eb16899-5121-790b-e5a3-192122ec0145/888735944840.png/1000x1000bb.jpg'
                }
            ],
            'artist_pic': 'https://pbs.twimg.com/media/F5qW_YWbQAAWpJ6?format=jpg&name=4096x4096',
            'artist_logo': 'https://i.pinimg.com/564x/1f/26/7c/1f267c307f318adbfb2744a48b8360c4.jpg'
        }
    ]


# Function untuk main page
def show_main(request: HttpRequest) -> HttpResponse:
    # Create a dictionary with the data
    data = {
        'nama': 'Yasmine Putri Viryadhani',
        'npm': '2206081862',
        'kelas': 'PBP A',
        'nama_app': 'kpop-albums',
    }

    template_name = 'main.html'

    # Sort the artists alphabetically based on their names
    sorted_artists = sorted(get_artist_data(), key=lambda artist: artist['artist'])

    # Get the current date
    current_date = datetime.now().date()

    # Seed the random number generator with the day's date
    random.seed(current_date.day)

    # Get a random artist name
    random_artist = random.choice(sorted_artists)

    # Get a random album name from the selected artist
    random_album = random.choice(random_artist['albums'])

    # Retrieve the list of artist names for the artists list
    artist_names = [artist['artist'] for artist in sorted_artists]

    # Pass the sorted artists list to the template
    return render(request, template_name, {'data': data, 'random_artist': random_artist, 'random_album': random_album,
                                           'artist_names': artist_names, 'contexts': sorted_artists})

# Function untuk artists' pages
def show_artist_detail(request: HttpRequest, artist_name: str) -> HttpResponse:
    # Find the artist data by artist_name from the contexts list
    artist_data = None

    for context in get_artist_data():
        if context['artist'] == artist_name:
            artist_data = context
            break
    
    if artist_data is None:
        return HttpResponse("Artist not found", status=404)
    
    template_name = 'artists.html'
    return render(request, template_name, {'artist_data': artist_data})

# Function untuk albums' pages
def show_album_detail(request, artist_name, album_name):
    # Find the album data by artist_name and album_name from the contexts list
    artist_data = None
    album_data = None

    for context in get_artist_data():
        if context['artist'] == artist_name:
            artist_data = context
            for album in context['albums']:
                if album['name'] == album_name:
                    album_data = album
                    break
            if album_data:
                break

    if artist_data is None or album_data is None:
        return HttpResponse("Artist or album not found", status=404)

    template_name = 'albums.html'
    return render(request, template_name, {'artist_data': artist_data, 'album_data': album_data})

def show_full_list(request):
    # Sort the artists alphabetically based on their names
    sorted_artists = sorted(get_artist_data(), key=lambda artist: artist['artist'])

    # Pass the sorted list of artists to the template
    return render(request, 'full_list.html', {'artists': sorted_artists})
