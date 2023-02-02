// //https://developer.mozilla.org/ja/docs/Web/API/Response#ajax_%E5%91%BC%E3%81%B3%E5%87%BA%E3%81%97
// //https://blog.share-wis.com/javascript-async-await#toc3
// //Github: "https://api.github.com/users/Tak2009/repos"

const django_1_language = "https://api.github.com/repos/Tak2009/django-1/languages";
const login = "https://tak2009.pythonanywhere.com/api/v1/auth/login/";
const pic_url = "https://tak2009.pythonanywhere.com/api/v1/pics/pics/";

const getLang = async (url) => {
    const response = await fetch(url); // Response オブジェクトを生成する
    if (response.ok) {
      const jsonValue = await response.json(); // レスポンスの本体から JSON の値を取得
      return Promise.resolve(jsonValue);
    } else {
      return Promise.reject('***Not Found');
    }
  }

// const postLogin = async (url, data)  => {
// // Default options are marked with *
//     const response = await fetch(url, {
//         method: 'POST', // *GET, POST, PUT, DELETE, etc.
//         mode: 'cors', // no-cors, *cors, same-origin
//         cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
//         credentials: 'include', // include, *same-origin, omit
//         headers: {
//         'Content-Type': 'application/json',
      
//         // 'Content-Type': 'application/x-www-form-urlencoded',
//         },
//         redirect: 'follow', // manual, *follow, error
//         referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
//         body: JSON.stringify(data) // body data type must match "Content-Type" header
//     });
//     return response.json(); 
// }

// const postPic = async (url, token, file, title)  => {
//     const form_data = new FormData();
//     console.log(typeof(file))

//     let blob = new Blob(file, "image/gif");
//     console.log(blob)
//     // https://developer.mozilla.org/ja/docs/Web/API/FormData/Using_FormData_Objects
//     // form_data.append('pic', blob)
//     form_data.append('title', title)
//     // Default options are marked with *
//         const response = await fetch(url, {
//             method: 'POST', // *GET, POST, PUT, DELETE, etc.
//             mode: 'cors', // no-cors, *cors, same-origin
//             cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
//             credentials: 'include', // include, *same-origin, omit
//             headers: {
//             // 'Content-Type': 'application/json',
//             'Authorization' : 'Token ' + token,
//             // 'Content-Type': 'multipart/form-data'
//             },
//             redirect: 'follow', // manual, *follow, error
//             referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
//             body: form_data, // body data type must match "Content-Type" header
//         });
//         return response.json(); // parses JSON response into native JavaScript objects
//     }


API = {getLang, postLogin, postPic};