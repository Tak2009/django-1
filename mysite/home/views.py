from django.shortcuts import  render, redirect
from django.views import View
from django.conf import settings
from django.contrib import messages  
from django.urls import reverse_lazy
from django.contrib.auth import login
from home.forms import NewUserForm


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