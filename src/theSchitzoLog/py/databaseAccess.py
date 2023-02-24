import pg8000 as pg

currentPlaylist = "playlist1"

####################################################
#    _____        _        _                       #
#   |  __ \      | |      | |                      #
#   | |  | | __ _| |_ __ _| |__   __ _ ___  ___    #
#   | |  | |/ _` | __/ _` | '_ \ / _` / __|/ _ \   #
#   | |__| | (_| | || (_| | |_) | (_| \__ \  __/   #
#   |_____/ \__,_|\__\__,_|_.__/ \__,_|___/\___|   #
#                                                  #
####################################################  

# with open('./py/loginInfo.txt', "r") as textInfo:
#     loginInfo = textInfo.readlines()
#     for a in enumerate(loginInfo):
#         loginInfo[a[0]] = loginInfo[a[0]].replace("\n", "")

client = pg.connect(
   database = "mhrahked",
   user = "mhrahked", 
   password = "SQAsoEhXFmHwC3Z8jlZWGpBr2WO2gmwz",
   host = "kashin.db.elephantsql.com",
   port = 5432
).cursor()

# client = pg.connect(
#    database = loginInfo[0],
#    user = loginInfo[1], 
#    password = loginInfo[2],
#    host = loginInfo[3],
#    port = loginInfo[4]
# ).cursor()

#############################################################
#    ______                    _    _                       #
#   |  ____|                  | |  (_)                      #
#   | |__  _   _  _ __    ___ | |_  _   ___   _ __   ___    #
#   |  __|| | | || '_ \  / __|| __|| | / _ \ | '_ \ / __|   #
#   | |   | |_| || | | || (__ | |_ | || (_) || | | |\__ \   #
#   |_|    \__,_||_| |_| \___| \__||_| \___/ |_| |_||___/   #
#                                                           #
#############################################################


def errorMessage(err:str):
    if len(err) == 0:
        print(f"Something Fucked Up\n\nEmpty Error")
        exit
    else:
        print(f"Something Fucked Up\n\n{err}")
        exit


def getData(currentPlaylist:str) -> list:
    client.execute(f"SELECT * FROM {currentPlaylist}")
    query = client.fetchall()
    data = []
    for a in query:
        data += [{
            'id': f'{a[0]}',
            'songName': f'{a[1]}',
            'artist': f'{a[2]}'
        }]
    return data

def putIntoTable(data:list) -> str:
    out = str()
    for a in data:
        out = out + f"""
        <tr>
            <td>{a["id"]}</td>
            <td>{a["songName"]}</td>
            <td>{a["artist"]}</td>
        </tr>""" 
    return (out)

