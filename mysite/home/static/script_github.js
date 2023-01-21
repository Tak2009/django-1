// https://htmlcolorcodes.com/color-picker/
background = ['#07FFD2', '#07B0FF', '#0734FF', '#5607FF', '#D207FF', '#FF07B0']

const renderLang = (langs) => {
    const num_array = Object.values(langs)
    const sum = num_array.reduce((accumulator, current) => accumulator + current);
    const lang_list = document.getElementById('skill');
    lang_index = 0
    for (lang in langs) {
        const div = document.createElement("div")
        div.classList.add("progress")
        div.style.backgroundColor = '#b6bfb6'
        console.log(lang_index, lang)
        ratio = (parseFloat(langs[lang])/sum * 100).toFixed(1)
        div.innerHTML = `<div class="progress-bar" role="progressbar" style="width: ${ratio}%; background:${background[lang_index % 6]}; color:white" aria-valuenow="${ratio * 100}" aria-valuemin="0" aria-valuemax="100">${lang}(${ratio})%</div>`
        lang_list.appendChild(div)
        lang_index += 1
    }
}

API.getLang(django_1_language).then(data => renderLang(data)).catch(console.log).finally(console.log("done"));;

// API.getLang(django_1_language)
// // 成功した場合は取得したリソースのテキストを出力
// .then(resp) => {
//   console.log(resp);
// })
// // 失敗した場合はエラーを出力
// .catch((error) => {
//   console.warn(error);
// });



// renderLang(langs)