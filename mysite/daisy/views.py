#from django.shortcuts import render

# Create your views here.

from daisy.models import Pic, Comment
from onestop.owner import OwnerListView, OwnerDetailView, OwnerDeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.humanize.templatetags.humanize import naturaltime

class PicListView(View):

    template_name = "daisy/daisy_list.html"

    def get(self, request):
        flash_list = Pic.objects.all().order_by('-created_at')[:5]
        print(flash_list[0])
        update_list = Pic.objects.exclude(pic="").order_by('-updated_at')[:5]
        ctx = {'flash_list' : flash_list, 'update_list': update_list}
        return render(request, self.template_name, ctx)

