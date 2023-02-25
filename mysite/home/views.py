from django.shortcuts import  render, redirect
from django.views import View
from django.conf import settings
from django.contrib import messages  
from django.urls import reverse_lazy
from django.contrib.auth import login
from home.forms import NewUserForm
import asyncio
import aiohttp
import time
from django.utils.decorators import classonlymethod
from asgiref.sync import sync_to_async
##Rate Limit: https://docs.github.com/en/rest/overview/resources-in-the-rest-api?apiVersion=2022-11-28#rate-limiting
## To check the rate limit 
## curl -i -H "Authorization: token YOUR_TOKEN" https://api.github.com/repos/Tak2009/django-1/languages
from mysite.settings import PERSONAL_ACCESS_TOKEN


class HomeView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal
        }
        return render(request, 'home/main.html', context)


# Step 1: Func based async. then connverted to Class based 
# https://www.youtube.com/watch?v=28KFBqi2JrA&list=RDCMUC1mxuk7tuQT2D0qTMgKji3w&start_radio=1&rv=28KFBqi2JrA&t=0
class TechView(View):
    template_name = "home/tech_list_dj_asyn_version.html"
    urls = [
        "https://api.github.com/repos/Tak2009/django-1/languages",
        "https://api.github.com/repos/Tak2009/raspi-2-motion-detect-sensor-oauth2-tk/languages",
        "https://api.github.com/repos/Tak2009/raspi-3-moisture-sensor-client-tk/languages",
        "https://api.github.com/repos/Tak2009/raspi-3-water-pump-server-tk/languages"
    ]

    ## Step2: The view home.views.view didn't return an HttpResponse object. It returned an unawaited coroutine instead. You may need to add an 'await' into your view.
    ## https://medium.com/@bruno.fosados/django-async-class-based-views-acbv-5986c4511ae6 ####
    ## https://stackoverflow.com/questions/62038200/correct-way-to-use-async-class-based-views-in-django ####
    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view
    ##

    ## Step 3: https://stackoverflow.com/questions/5376985/django-request-user-is-always-anonymous-user
    ## You cannot call this from an async context - use a thread or sync_to_async at {% if user.is_authenticated %}
    @sync_to_async
    def get_user_from_request(self, request):
        return request.user if bool(request.user) else None
    ##

    async def get_github(self, session, url):
        async with session.get(url) as res:
            github_data = await res.json()
            return {url: github_data}
    
    def CalcRatio(self, languages_dict):
        total = sum((languages_dict.values()))
        lang_ratio_by_project = {}
        for lang in languages_dict:
             lang_ratio_by_project[lang] = "{}".format(round(int(languages_dict[lang])/total * 100, 2))
        return lang_ratio_by_project

    async def get(self, request):
        starting_time = time.time()
        actions = []
        github_data_list = []
        project_list = {}

        ## Step3: https://stackoverflow.com/questions/5376985/django-request-user-is-always-anonymous-user
        ## You cannot call this from an async context - use a thread or sync_to_async at {% if user.is_authenticated %}
        user = await self.get_user_from_request(request)
        ##

        headers={"Authorization": "token " + PERSONAL_ACCESS_TOKEN}
        async with aiohttp.ClientSession(headers=headers) as session:
            for url in self.urls:
                actions.append(asyncio.ensure_future(self.get_github(session, url)))
            github_res = await asyncio.gather(*actions)
            for data in github_res:
                github_data_list.append(data)
        count = len(github_data_list)
        total_time = time.time() - starting_time
    
        # change the data structure
        for i, v in enumerate(github_data_list):
            print(i, v)
            old_key = list(v.keys())[0]
            new_key = old_key[old_key.find('Tak2009/')+len('Tak2009/'): -len('/languages')]
            # calc ratio
            lang_ratio_by_project = self.CalcRatio(v[old_key])
            project_list[new_key] = lang_ratio_by_project
        # print(project_list)
            
        return render(
            request,
            self.template_name,
            {"project_list": project_list, "count": count, "process_time": total_time},
        )


def register(request):
	template_name = "home/register.html"
	success_url = reverse_lazy('home:all')
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect(success_url)
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	context={"form":form}
	return render (request, template_name, context)


