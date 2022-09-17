import asyncio
import json
from multiprocessing.util import is_exiting
from time import sleep
import httpx 
from bs4 import BeautifulSoup as bs
from metacritic_parser import req

from targetparser import parseNewReleases
from vkbot import bot_broadcasting

config = open("configuration.json", 'r')
serialized = json.load(config)
account = serialized["Account"]
type = account["Type"]
token = account["Name"]
genre = serialized["Genre"].lower()
enableSchedudling = serialized["isEnadbleSchedudler"]
enableBroadcasting = serialized["isEnableBroadcastToAccounts"]
lastAlbum = serialized["NameOfLastAlbum"]

#ВАЖНО любой парсер должен возратить состояние: есть ли новые албомы

is_exiting_new_albums = asyncio.run(req(lastReleasae=lastAlbum,genre=genre))


albums = open("albums2.json","r")

bot_broadcasting(is_exiting_new_albums,albums,genre,token)