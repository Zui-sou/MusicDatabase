const {Client} = require('pg')
const fs = require('fs')
const $ = require('jquery')


/////////////////////////////////////////////////////////////
//   __      __           _         _      _               //
//   \ \    / /          (_)       | |    | |              //
//    \ \  / /__ _  _ __  _   __ _ | |__  | |  ___  ___    //
//     \ \/ // _` || '__|| | / _` || '_ \ | | / _ \/ __|   //
//      \  /| (_| || |   | || (_| || |_) || ||  __/\__ \   //
//       \/  \__,_||_|   |_| \__,_||_.__/ |_| \___||___/   //
//                                                         //
/////////////////////////////////////////////////////////////

var loginLink = fs.readFileSync("link.txt").toString();
var client = new Client(loginLink)
var currentPlaylist = "playlist1"


///////////////////////////////////////////////////////////////
//    ______                    _    _                       //
//   |  ____|                  | |  (_)                      //
//   | |__  _   _  _ __    ___ | |_  _   ___   _ __   ___    //
//   |  __|| | | || '_ \  / __|| __|| | / _ \ | '_ \ / __|   //
//   | |   | |_| || | | || (__ | |_ | || (_) || | | |\__ \   //
//   |_|    \__,_||_| |_| \___| \__||_| \___/ |_| |_||___/   //
//                                                           //
///////////////////////////////////////////////////////////////

function errorMessage(err){
    console.log(`Something Fucked Up\n\n${err}`)
}

/*
async function getData() {


        await client.connect()
        console.log("Connected")
        const playlist = await client.query(`select * from ${currentPlaylist}`)
        console.table(playlist.rows)
        let out = "";
        for(let i = 0; i < playlist.rowCount; i++) {
            out += `
                <tr>
                    <td>${playlist.rows[i].id}</td>
                    <td>${playlist.rows[i].song_name}</td>
                    <td>${playlist.rows[i].artist}</td>
                </tr>
            `
*/
/////////////////////////////////////////////
//     _____              _         _      //
//    / ____|            (_)       | |     //
//   | (___    ___  _ __  _  _ __  | |_    //
//    \___ \  / __|| '__|| || '_ \ | __|   //
//    ____) || (__ | |   | || |_) || |_    //
//   |_____/  \___||_|   |_|| .__/  \__|   //
//                          | |            //
//                          |_|            //
/////////////////////////////////////////////

/*
await fs.readFile('loginInfo.json', 'utf8', (err, fileData) => {
    if (err) {
        errorMessage(err)
        return
    }
    loginLink = JSON.stringify(JSON.parse(fileData).link)
    console.log(loginLink)
    return loginLink
})
*/

$(document).ready(function(){
    alert("amit")
 });

client.connect()
.then(() => client.query (`select * from ${currentPlaylist}`))
.then(results => console.table(results.rows))
.catch(err => errorMessage(err))
.finally(() => client.end())
