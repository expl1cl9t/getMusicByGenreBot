import asyncio
import json
from platform import release
import re
import httpx 
from bs4 import BeautifulSoup as bs

from album_output import album_output


async def req(lastReleasae, genre):
    with httpx.Client(headers={'user-agent': 'my-app/0.0.1'}) as client:
        r = client.get("https://www.metacritic.com/browse/albums/release-date/new-releases/date?view=condensed")

        source = bs(r.text,'html.parser')

        links = source.find_all('a',"title")

        ln = len(links)

        a = 0

        

#получил массив из ссылок

    releases = [] #заготовка под будущие релизы

    for i in links:
        async with httpx.AsyncClient(headers={'user-agent': 'my-app/0.0.1'}) as next_clients:
            try:
                item = album_output()
                request = "https://www.metacritic.com" + i["href"]
                r2 = await next_clients.get(request)
                mn_cont = bs(r2.text,'html.parser')
                item.Title = mn_cont.find("a","hover_none").text.strip()
                if item.Title == lastReleasae:
                    break
                item.Authors = mn_cont.find("span","band_name").text.strip()
                item.Genre = re.sub(" +"," ",mn_cont.find("li","summary_detail product_genre").text.replace("Genre(s)","").strip())
                if not genre in item.Genre.lower():
                    continue
                item.releaseDate = mn_cont.find("li","summary_detail release").text.strip().replace("Release Date:","").replace("\n","")
                #print("Название: " + name + '\n' + "Автор: " + author + '\n' + "Жанр: " + re.sub(" +"," ",genre) + '\n' +re.sub(" +"," ",date) + '\n' + "-----------------------------" + '\n')
                releases.append(item)
                a+=1
                print("Выполнено " + str(a) + " из " + str(ln) + '\n')
            except Exception as e:
                print(e)
    if len(releases) == 0:
        return False
    else:
        serilized = json.dumps(releases, default=lambda x : x.__dict__)
        f = open("albums2.json",'w',encoding="utf-8")
        f.write(serilized)
        f2 = open("configuration.json","r")
        dt = json.load(f2)
        dt["NameOfLastAlbum"] = releases[0].Title
        with open("configuration.json","w") as f3:
            json.dump(dt,f3)
        return True
#asyncio.run(req())