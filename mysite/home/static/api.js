// //https://developer.mozilla.org/ja/docs/Web/API/Response#ajax_%E5%91%BC%E3%81%B3%E5%87%BA%E3%81%97
// //https://blog.share-wis.com/javascript-async-await#toc3
// //Github: "https://api.github.com/users/Tak2009/repos"

const django_1_language = "https://api.github.com/repos/Tak2009/django-1/languages";

const getLang = async (url) => {
    const response = await fetch(url); // Response オブジェクトを生成する
    if (response.ok) {
      const jsonValue = await response.json(); // レスポンスの本体から JSON の値を取得
      return Promise.resolve(jsonValue);
    } else {
      return Promise.reject('***Not Found');
    }
  }

API = {getLang};