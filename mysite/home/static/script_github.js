// https://htmlcolorcodes.com/color-picker/
// https://qiita.com/7note/items/4d922ebd33dbefe99a89
background = ['#07FFD2', '#07B0FF', '#0734FF', '#5607FF', '#D207FF', '#FF07B0']

const renderLang = (langs) => {
    const num_array = Object.values(langs)
    const sum = num_array.reduce((accumulator, current) => accumulator + current);
    const lang_list = document.getElementById('skill');
    lang_index = 0
    for (lang in langs) {
        const div = document.createElement("div")
        div.classList.add("progress")
        div.style.backgroundColor = '#f59842'
        div.style.height= '30px'

        console.log(lang_index, lang)
        ratio = (parseFloat(langs[lang])/sum * 100).toFixed(1)
        div.innerHTML = 
            `<div class="progress-bar" role="progressbar" style="width: ${ratio}%; background:${background[lang_index % 6]}" aria-valuenow="${ratio * 100}" aria-valuemin="0" aria-valuemax="100" onMouseOut="this.style.background='${background[lang_index % 6]}';" onMouseOver="this.style.background='#EEF';">
                <a href="https://github.com/Tak2009/django-1/search?l=${lang.toLowerCase()}" target="_blank" style="color: #f7f5f5" onMouseOut="this.style.color='#f7f5f5';" onMouseOver="this.style.color='#050505';">
                    ${lang}(${ratio})%
                </a>
            </div>`
        lang_list.appendChild(div)
        lang_index += 1
    }
}

API.getLang(django_1_language).then(data => renderLang(data)).catch(console.log).finally(console.log("done"));;

API.postLogin(login, {
    "username" : "tak_superman_2023",
    "password": "amsuper07112023"
    }
    ).then(data => console.log(data)).catch(console.log).finally(console.log("done"));;

// API.getLang(django_1_language)
// // 成功した場合は取得したリソースのテキストを出力
// .then(resp) => {
//   console.log(resp);
// })
// // 失敗した場合はエラーを出力
// .catch((error) => {
//   console.warn(error);
// });

