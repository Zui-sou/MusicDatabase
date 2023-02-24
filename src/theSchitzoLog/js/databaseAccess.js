const {Client} = require('pg')

//var loginLink = fs.readFileSync("").toString();
var client = new Client("postgresql://postgres:123@localhost:5432/postgres")
var currentPlaylist = "playlist1"

/*
fetch("link1.txt")
.then(res => res.text)
.then(text => console.log(text))
*/
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

let out = ``;
function getData() {
    client.connect()
    .then(() => client.query (`select * from ${currentPlaylist}`))
    .then(data => {for(let i = 0; i < data.rowCount; i++) {
        out += `
            <tr>
                <td>${data.rows[i].id}</td>
                <td>${data.rows[i].song_name}</td>
                <td>${data.rows[i].artist}</td>
            </tr>
            `
        }
    })
//    .then(() => document.getElementById("tableData").innerHTML = out)
    .then(() => console.log(out))
    .catch(err => errorMessage(err))
    .finally(() => client.end())
}

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

getData()