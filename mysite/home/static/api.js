// //https://developer.mozilla.org/ja/docs/Web/API/Response#ajax_%E5%91%BC%E3%81%B3%E5%87%BA%E3%81%97
// //https://blog.share-wis.com/javascript-async-await#toc3
// //Github: "https://api.github.com/users/Tak2009/repos"
// //Rate Limit: https://docs.github.com/en/rest/overview/resources-in-the-rest-api?apiVersion=2022-11-28#rate-limiting

const project_urls = [
    "https://api.github.com/repos/Tak2009/django-1/languages",
    "https://api.github.com/repos/Tak2009/raspi-2-motion-detect-sensor-oauth2-tk/languages",
    "https://api.github.com/repos/Tak2009/raspi-3-moisture-sensor-client-tk/languages",
    "https://api.github.com/repos/Tak2009/raspi-3-water-pump-server-tk/languages"
]


const getProjects = async (url_list) => {
    const detail_by_project = {}
    serch_keyword_beg = 'Tak2009/'
    serch_keyword_end = '/languages'
    for (url of url_list) {
        const project_name = url.slice(url.search(serch_keyword_beg) + serch_keyword_beg.length, url.search(serch_keyword_end))
        const response = await fetch(url); // Response オブジェクトを生成する
        console.log(url)
        if (response.ok) {
          const jsonValue = await response.json(); // レスポンスの本体から JSON の値を取得
          detail_by_project[project_name] = jsonValue;
        } else {
          return Promise.reject('***Not Found');
        }
    }
    return detail_by_project
}


API = {getProjects};

// const getProjects = async (url_list) => {
//     for (url of url_list) {
//         const response = await fetch(url); // Response オブジェクトを生成する
//         console.log(url)
//         if (response.ok) {
//           const jsonValue = await response.json(); // レスポンスの本体から JSON の値を取得
//           return Promise.resolve(jsonValue);
//         } else {
//           return Promise.reject('***Not Found');
//         }
//     }
// }