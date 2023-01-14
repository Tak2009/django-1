
// https://docs.djangoproject.com/en/4.1/howto/static-files/ 
// https://docs.djangoproject.com/en/4.1/ref/templates/builtins/#json-script
const inner_html_favorites = JSON.parse(document.getElementById('favorites-json').textContent);

// //https://notetoself-dy.com/javascript-variable-global-local/
var favorite_list = ""
const btn = document.getElementById('sort-favarite');

const test = () => {
    console.log(favorites)
}

window.addEventListener('load', () => {
  console.log('onload!');
  favorite_list = inner_html_favorites
})

// //1. to store favosite ids in favorite_list
// //https://adamj.eu/tech/2020/02/18/safely-including-data-for-javascript-in-a-django-template/
console.log('check3 ' + $j.fn.jquery);
function favPost(url, recipe_id) {
  console.log('Requesting JSON');
  // 2. manipulate dom first to update favorite_list variable
  if (url.includes("unfavorite")){
    const index = favorite_list.indexOf(recipe_id);
    const x = favorite_list.splice(index, 1);
    // console.log(favorite_list)
  } else {
    favorite_list.push(recipe_id)
    // console.log(favorite_list)
  }
  $j.post(url, {},  function(rowz){
      console.log(url, 'finished');
      $("#unfavorite_star_"+recipe_id).toggle();
      $("#favorite_star_"+recipe_id).toggle();
  }).fail(function(xhr) {
      alert('Url failed with '+xhr.status+' '+url);
  });
}

btn.addEventListener('click', () => {
  let list_element = document.getElementById("registered-recipe-list");
  let length = list_element.childElementCount;
  console.log('clicked!');
  // console.log(list_element);
  // console.log(length);
  for(let i=0; i<length; i++) {
    console.log(parseInt(list_element.children[i].id, 10));
    if (favorite_list.includes(parseInt(list_element.children[i].id, 10))) {
      console.log('Yes!');
    } else {
    console.log('No!');
    list_element.children[i].style.display = "none"
    }
  }
}, false);

// //https://www.buildinsider.net/web/jqueryref/068
// original
// console.log('check3 ' + $j.fn.jquery);
// function favPost(url, recipe_id) {
//     console.log('Requesting JSON');
//     $j.post(url, {},  function(rowz){
//         console.log(url, 'finished');
//         $("#unfavorite_star_"+recipe_id).toggle();
//         $("#favorite_star_"+recipe_id).toggle();
//     }).fail(function(xhr) {
//         alert('Url failed with '+xhr.status+' '+url);
//     });
// }
