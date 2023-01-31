from sclib import SoundcloudAPI, Playlist
from datetime import date
import psycopg2
import json


playlistLink = str(input(f'Gib Link\n >> '))
tableID = str
playlistName = str
songCount = int



####################################################
#    _____        _        _                       #
#   |  __ \      | |      | |                      #
#   | |  | | __ _| |_ __ _| |__   __ _ ___  ___    #
#   | |  | |/ _` | __/ _` | '_ \ / _` / __|/ _ \   #
#   | |__| | (_| | || (_| | |_) | (_| \__ \  __/   #
#   |_____/ \__,_|\__\__,_|_.__/ \__,_|___/\___|   #
#                                                  #
####################################################                                    


with open('loginInfo.txt', "r") as textInfo:
    loginInfo = textInfo.readlines()
    for a in enumerate(loginInfo):
        loginInfo[a[0]] = loginInfo[a[0]].replace("\n", "")

import psycopg2
conct = psycopg2.connect(
   database = loginInfo[0],
   user = loginInfo[1], 
   password = loginInfo[2],
   host = loginInfo[3],
   port = loginInfo[4]
)

print('Connection Successful')

cur = conct.cursor()



#####################################################
#    ______                _   _                    #
#   |  ____|              | | (_)                   #
#   | |__ _   _ _ __   ___| |_ _  ___  _ __  ___    #
#   |  __| | | | '_ \ / __| __| |/ _ \| '_ \/ __|   #
#   | |  | |_| | | | | (__| |_| | (_) | | | \__ \   #
#   |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/   #
#                                                   #
#####################################################


def makeIDTableEntry():
   cur.execute(f"""
   INSERT INTO "playlistIDs" (playlist_name,song_count,last_update) 
   VALUES (null,null,null)
   """)
   print("Entry Made")


def makeNewTable(tableID: str) -> str:
   tableID = cur.execute("""
   SELECT "id" FROM "playlistIDs"
   ORDER BY "id" DESC 
   LIMIT 1;
   """)
   tableID = (str(cur.fetchone())).replace(",","").replace("(","").replace(")","")
   cur.execute(f"""CREATE TABLE "{'playlist'+tableID}" (
      ID serial not null primary key,
      song_name varchar not null,
      artist varchar not null
      )"""
   )
   print("Table Made")
   return(tableID)


def playlistScraper(playlistLink: str) -> list:
   api = SoundcloudAPI()
   playlist = api.resolve(playlistLink)
   assert type(playlist) is Playlist
   for track in playlist.tracks:
      yield(track)
   print("Table Populated")


def updateIDTable(playlistLink: str, tableID: str):
   api = SoundcloudAPI()
   playlist = api.resolve(playlistLink)
   assert type(playlist) is Playlist
   playlistName = str(playlist.title)
   songCount = int(playlist.track_count)
   todaysDate = str(date.today()).split("-")
   todaysDate = todaysDate[1] + "/" + todaysDate [2] + "/" + todaysDate[0]
   cur.execute(f"""
   UPDATE "playlistIDs"
	SET playlist_name = '{playlistName}', song_count = {songCount}, last_update = '{todaysDate}'
   WHERE id = {tableID}
   """)
   print("ID Table Updated")



######################################
#     _____           _       _      #
#    / ____|         (_)     | |     #
#   | (___   ___ _ __ _ _ __ | |_    #
#    \___ \ / __| '__| | '_ \| __|   #
#    ____) | (__| |  | | |_) | |_    #
#   |_____/ \___|_|  |_| .__/ \__|   #
#                      | |           #
#                      |_|           #
######################################


if __name__ == "__main__":
   makeIDTableEntry()
   tableID = makeNewTable(playlistLink)
   for a in playlistScraper(playlistLink):
      cur.execute(f"""
      INSERT INTO {'playlist'+tableID} (song_name,artist) 
      VALUES ('{(a.title).replace("'","")}','{(a.artist).replace("'","")}');
      """)
   updateIDTable(playlistLink, tableID)
   conct.commit()
   conct.close()