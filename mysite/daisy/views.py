#from django.shortcuts import render

# Create your views here.

#from daisy.models import Ad, Comment, Fav
from ads.owner import OwnerListView, OwnerDetailView, OwnerDeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
#from django.contrib.auth.mixins import LoginRequiredMixin
#from django.urls import reverse_lazy, reverse
#from daisy.forms import CreateForm, CommentForm
#from django.http import HttpResponse
#from django.db.models import Q
from django.contrib.humanize.templatetags.humanize import naturaltime

class PicListView(View):

    template_name = "daisy/pic_list.html"

    def get(self, request) :

        # favorites = list()
        # print(request.path)
        # # creating ad_list based on 1 if there is a serch string
        # strval =  request.GET.get("search", False)
        # if strval:
        #     query = Q(title__icontains=strval)
        #     query.add(Q(text__icontains=strval), Q.OR)
        #     ad_list = Ad.objects.filter(query).select_related().order_by('-updated_at')[:10]
        # # or no search string
        # else :
        #     ad_list = Ad.objects.all().order_by('-updated_at')[:10]

        # for obj in ad_list:
        #     obj.natural_updated = naturaltime(obj.updated_at)

        # # adding favorite stars
        # if request.user.is_authenticated:
        #     # rows = [{'id': 2}, {'id': 4} ... ]  (A list of rows)
        #     rows = request.user.favorite_ads.values('id')
        #     # favorites = [2, 4, ...] using list comprehension
        #     favorites = [ row['id'] for row in rows ]
        #     print(favorites)
        # ctx = {'pic_list' : pic_list, 'favorites': favorites, "search": strval}
        ctx = {'pic_list' : pic_list, "search": strval}
        return render(request, self.template_name, ctx)