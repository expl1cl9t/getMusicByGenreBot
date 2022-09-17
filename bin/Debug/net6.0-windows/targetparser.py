import json
import re
import httpx 
from bs4 import BeautifulSoup as bs

from album_output import album_output

template = {"nothing" : "Ничего нового"}

def parseNewReleases(genre, lastAlbum):
    
    isExistsAlbum = True

    r = httpx.get("https://rateyourmusic.com/new-music/")

    source = bs(r.text, 'html.parser')

    releases = source.find_all("div", re.compile("newreleases_itembox excl_item release_\d{0,20} artist_\d{0,20}"))

    albums = []


    for i in range(0,len(releases) - 1):
        album = album_output()
        album.Title = releases[i].find("a","album newreleases_item_title").text
        album.Authors = releases[i].find("span","newreleases_item_artist").text
        album.releaseDate = releases[i].find("div","newreleases_item_releasedate").text
        album.Genre = releases[i].find("div","newreleases_item_textbox_genre").text.replace("\n","")
        albums.append(album)

    satisfied_albums = []
    satisfied2_albums = []
    for i in albums:
        if genre in i.Genre.lower():
            satisfied2_albums.append(i)
    for i in satisfied2_albums:
        if i.Title != lastAlbum:
            satisfied_albums.append(i)
        else:
            break
    print(len(satisfied_albums))
    if len(satisfied_albums) == 0:
        satisfied_albums = template
        isExistsAlbum = False
        return isExistsAlbum
    if lastAlbum == satisfied_albums[0].Title:
        satisfied_albums = template
        isExistsAlbum = False
        return isExistsAlbum
    serilized = json.dumps(satisfied_albums, default=lambda x : x.__dict__)
    f = open("albums2.json",'w',encoding="utf-8")
    f.write(serilized)
    f2 = open("configuration.json","r")
    dt = json.load(f2)
    dt["NameOfLastAlbum"] = satisfied_albums[0].Title
    with open("configuration.json","w") as f3:
        json.dump(dt,f3)
