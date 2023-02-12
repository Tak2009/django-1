
// https://docs.djangoproject.com/en/4.1/howto/static-files/ 
// https://docs.djangoproject.com/en/4.1/ref/templates/builtins/#json-script
const inner_html_upload_field = JSON.parse(document.getElementById('upload-field-name').textContent);
const inner_htmlmax_upload = JSON.parse(document.getElementById('max-upload-limit').textContent);

// https://stackoverflow.com/questions/2472422/django-file-upload-size-limit
$("#upload_form").submit(function() {
  console.log('Checking file size');
  console.log('check6 ' + $j.fn.jquery);
  console.log('check7 ' + $.fn.jquery);
  if (window.File && window.FileReader && window.FileList && window.Blob) {
      var file = $('#id_' + inner_html_upload_field)[0].files[0];
      if (file && file.size > inner_htmlmax_upload ) {
          alert("File " + file.name + " of type " + file.type + " must be < " + inner_htmlmax_upload);
      return false;
    }
  }
});

