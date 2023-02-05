from django import forms
from onestop.models import Recipe
from django.core.files.uploadedfile import InMemoryUploadedFile
from onestop.humanize import naturalsize
from taggit.forms import TagField

# override django-taggit tags so that they are always lowercase
# https://github.com/jazzband/django-taggit/blob/master/taggit/forms.py
# https://docs.djangoproject.com/en/4.1/ref/forms/validation/
# https://stackoverflow.com/questions/24313201/convert-all-charfield-form-field-inputs-to-lowercase-in-django-forms
class TagCustomField(TagField):
    def to_python(self, value):
        return value.lower()


class CreateForm(forms.ModelForm):
    max_upload_limit = 2 * 1024 * 1024
    max_upload_limit_text = naturalsize(max_upload_limit)
    picture = forms.FileField(required=False, label='File to Upload <= '+max_upload_limit_text)
    upload_field_name = 'picture'

    # override django-taggit tags so that they are always lowercase
    tags = TagCustomField()

    class Meta:
        model = Recipe
        fields = ['title', 'text', 'website', 'picture', 'tags']  # Picture is manual

    # Validate the size of the picture
    def clean(self):
        cleaned_data = super().clean()
        pic = cleaned_data.get('picture')
        if pic is None:
            return
        if len(pic) > self.max_upload_limit:
            self.add_error('picture', "File must be < "+self.max_upload_limit_text+" bytes")

    # Convert uploaded File object to a picture
    def save(self, commit=True):
        instance = super(CreateForm, self).save(commit=False)

        # We only need to adjust picture if it is a freshly uploaded file
        f = instance.picture   # Make a copy
        if isinstance(f, InMemoryUploadedFile):  # Extract data from the form to the model
            bytearr = f.read()
            instance.content_type = f.content_type
            instance.picture = bytearr  # Overwrite with the actual image data
        if commit:
            # https://django-taggit.readthedocs.io/en/latest/forms.html#commit-false
            self.save_m2m()
            instance.save()
                
        return instance

# https://docs.djangoproject.com/en/3.0/topics/http/file-uploads/
# https://stackoverflow.com/questions/2472422/django-file-upload-size-limit
# https://stackoverflow.com/questions/32007311/how-to-change-data-in-django-modelform
# https://docs.djangoproject.com/en/3.0/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other

class NoteForm(forms.Form):
    note = forms.CharField(required=True, max_length=500, min_length=3, strip=True)
