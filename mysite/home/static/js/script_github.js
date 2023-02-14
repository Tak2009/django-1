// https://htmlcolorcodes.com/color-picker/
// https://qiita.com/7note/items/4d922ebd33dbefe99a89
background = ['#07FFD2', '#07B0FF', '#0734FF', '#5607FF', '#D207FF', '#FF07B0']


const renderProject = (projects) => {
    const project_list = document.getElementById('project-list');
    const project_detail = document.getElementById('project-detail');
    let project_index = 0

    for (project in projects) {
        let project_li
        let project_div
        if (project_index == 0) {
            project_li = `<li data-target="#carouselExampleIndicators" data-slide-to=${project_index} class="active" />`
            project_div = 
                `<div class="carousel-item active">
                    <p style="margin-bottom: 0; margin-left: 2vw; margin-top: 0.5vw; color: white;"><strong>Repository Name: ${project}</strong></p>
                    <div class="container py-4" id=${project_index} style="display: inline-block; min-height: 20vh;"></div>
                </div>`
        } else {
            project_li = `<li data-target="#carouselExampleIndicators" data-slide-to=${project_index} />`
            project_div = 
                `<div class="carousel-item">
                    <p style="margin-bottom: 0; margin-left: 2vw; margin-top: 0.5vw; color: white;"><strong>Repository Name: ${project}</strong></p>
                    <div class="container py-4" id=${project_index} style="display: inline-block; min-height: 20vh;"></div>
                </div>`
        }
        project_list.innerHTML += project_li
        project_detail.innerHTML += project_div
        renderLanguagesByProject(projects[project], project_index, project)
        project_index += 1
    }
}


const renderLanguagesByProject = (project, project_index, project_name) => {
    const num_array = Object.values(project)
    const sum = num_array.reduce((accumulator, current) => accumulator + current);
    const project_index_div = document.getElementById((project_index).toString());
    lang_index = 0
    for (lang in project) {
        ratio = (parseFloat(project[lang])/sum * 100).toFixed(1)
        const div = document.createElement("div")
        div.classList.add("progress")
        div.style.backgroundColor = '#f59842'
        div.style.height= '30px'
        let lang_progress_bar_div = 
            `<div class="progress-bar" role="progressbar" style="width: ${ratio}%; background:${background[lang_index % 6]}" aria-valuenow="${ratio * 100}" aria-valuemin="0" aria-valuemax="100" onMouseOut="this.style.background='${background[lang_index % 6]}';" onMouseOver="this.style.background='#EEF';">
                <a href="https://github.com/Tak2009/${project_name}/search?l=${lang.toLowerCase()}" target="_blank" style="color: #f7f5f5" onMouseOut="this.style.color='#f7f5f5';" onMouseOver="this.style.color='#050505';">
                    <p style="margin-bottom: 0; margin-top: 0;">${lang}(${ratio})%</p>
                </a>
            </div>`
        div.insertAdjacentHTML("afterbegin", lang_progress_bar_div)
        project_index_div.appendChild(div)
        lang_index += 1
    }
}

API.getProjects(project_urls).then(projects => renderProject(projects)).catch(console.log).finally(console.log("done"));
