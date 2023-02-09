from onestop.models import Recipe, Note, Favo
from onestop.owner import OwnerDetailView, OwnerDeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from onestop.forms import CreateForm, NoteForm
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.humanize.templatetags.humanize import naturaltime
from taggit.models import Tag
from django.views.generic.list import ListView
# https://stackoverflow.com/questions/16458166/how-to-disable-djangos-csrf-validation
from django.views.decorators.csrf import csrf_exempt # for add and delete favorites
from django.utils.decorators import method_decorator # for add and delete favorites
from django.db.utils import IntegrityError # for add and delete favorites


class RecipeListView(View):
    # model = Recipe
    # By convention:
    template_name = "onestop/recipe_list.html"

    def get(self, request) :

        favorites = list()
        print(request.path)
        # creating recipe_list based on 1 if there is a serch string
        strval =  request.GET.get("search", False)
        if strval:
            query = Q(title__icontains=strval)
            query.add(Q(text__icontains=strval), Q.OR)
            recipe_list = Recipe.objects.filter(query).select_related().order_by('-updated_at')[:10]
        # or no search string
        else :
            recipe_list = Recipe.objects.all().order_by('-updated_at')[:10]

        for obj in recipe_list:
            obj.natural_updated = naturaltime(obj.updated_at)

        # adding favorite stars
        if request.user.is_authenticated:
            # rows = [{'id': 2}, {'id': 4} ... ]  (A list of rows)
            rows = request.user.favorite_recipes.values('id')
            # favorites = [2, 4, ...] using list comprehension
            favorites = [ row['id'] for row in rows ]

        ctx = {'recipe_list' : recipe_list, 'favorites': favorites, "search": strval}
        return render(request, self.template_name, ctx)


class RecipeDetailView(OwnerDetailView):
    model = Recipe
    template_name = "onestop/recipe_detail.html"
    
    def get(self, request, pk) :
        x = Recipe.objects.get(id=pk)
        notes = Note.objects.filter(recipe=x).order_by('-updated_at')
        note_form = NoteForm()
        context = { 'recipe' : x, 'notes': notes, 'note_form': note_form }
        return render(request, self.template_name, context)


class RecipeCreateView(LoginRequiredMixin, View):
    template_name = 'onestop/recipe_form.html'
    success_url = reverse_lazy('onestop:all')

    def get(self, request, pk=None):
        form = CreateForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        form = CreateForm(request.POST, request.FILES or None)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)
        # Add owner to the model before saving
        recipe = form.save(commit=False)
        recipe.owner = self.request.user
        recipe.save()
        # https://www.dj4e.com/assn/dj4e_ads4.md?PHPSESSID=bd08ca99d78434177e27b51978bafaf9
        # https://django-taggit.readthedocs.io/en/latest/forms.html#commit-false
        form.save_m2m()    # Add this for taggit
        return redirect(self.success_url)


class RecipeUpdateView(LoginRequiredMixin, View):
    template_name = 'onestop/recipe_form.html'
    success_url = reverse_lazy('onestop:all')

    def get(self, request, pk):
        recipe = get_object_or_404(Recipe, id=pk, owner=self.request.user)
        form = CreateForm(instance=recipe)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        recipe = get_object_or_404(Recipe, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=recipe)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)
        recipe = form.save(commit=False)
        recipe.save()
        # https://www.dj4e.com/assn/dj4e_ads4.md?PHPSESSID=bd08ca99d78434177e27b51978bafaf9
        # https://django-taggit.readthedocs.io/en/latest/forms.html#commit-false
        form.save_m2m()    # Add this for taggit
        return redirect(self.success_url)


class RecipeDeleteView(OwnerDeleteView):
    model = Recipe


def stream_file(request, pk):
    recipe = get_object_or_404(Recipe, id=pk)
    response = HttpResponse()
    response['Content-Type'] = recipe.content_type
    response['Content-Length'] = len(recipe.picture)
    response.write(recipe.picture)
    return response


class NoteCreateView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        f = get_object_or_404(Recipe, id=pk)
        note = Note(text=request.POST['note'], owner=request.user, recipe=f)
        note.save()
        return redirect(reverse('onestop:recipe_detail', args=[pk]))

class NoteDeleteView(OwnerDeleteView):
    model = Note
    template_name = "onestop/note_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        recipe = self.object.recipe
        return reverse('onestop:recipe_detail', args=[recipe.id])

class TagListView(ListView):
    model = Tag
    template_name = "onestop/tag_list.html"
    context_object_name = 'tag_list'


class RecipeByTagListView(ListView):
    # https://django-taggit.readthedocs.io/en/latest/api.html#filtering
    model = Tag
    template_name = "onestop/recipe_by_tag_list.html"
    context_object_name = 'recipes_by_tag_list'

    def get(self, request, name) :
        x = Tag.objects.get(name=name)
        print(x)
        recipes = Recipe.objects.filter(tags__name__in=[name]).order_by('-updated_at')
        context = {'recipes': recipes, 'tag_name' : name }
        return render(request, self.template_name, context)


def remove_all_tags_without_objects(request):
    success_url = reverse_lazy('onestop:tag_list')
    for tag in Tag.objects.all():
        if tag.taggit_taggeditem_items.count() == 0:
            print('Removing: {}'.format(tag))
            tag.delete()
        else:
            print('Keeping: {}'.format(tag))
    return redirect(success_url) 

# https://docs.djangoproject.com/en/4.1/topics/class-based-views/intro/#decorating-the-class
# https://docs.djangoproject.com/en/4.1/ref/csrf/#module-django.views.decorators.csrf
@method_decorator(csrf_exempt, name='dispatch')
class AddFavoView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        print("Add PK",pk)
        t = get_object_or_404(Recipe, id=pk)
        fav = Favo(user=request.user, recipe=t)
        try:
            fav.save()  # In case of duplicate key
        except IntegrityError as e:
            pass
        return HttpResponse()

@method_decorator(csrf_exempt, name='dispatch')
class DeleteFavoView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        print("Delete PK",pk)
        t = get_object_or_404(Recipe, id=pk)
        try:
            # fav = Fav.objects.get(user=request.user, ad=t).delete()
            Favo.objects.get(user=request.user, recipe=t).delete()
        except Favo.DoesNotExist as e:
            pass

        return HttpResponse()

