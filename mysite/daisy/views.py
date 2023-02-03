#from django.shortcuts import render

# Create your views here.

from daisy.models import Pic, Comment
from onestop.owner import OwnerListView, OwnerDetailView, OwnerDeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.humanize.templatetags.humanize import naturaltime
from daisy.forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse


class PicListView(View):

    template_name = "daisy/pic_list.html"

    def get(self, request):
        flash_list = Pic.objects.all().order_by('-created_at')[:5]
        print(flash_list[0])
        update_list = Pic.objects.exclude(pic="").order_by('-updated_at')[:5]
        ctx = {'flash_list' : flash_list, 'update_list': update_list}
        return render(request, self.template_name, ctx)


class PicDetailView(OwnerDetailView):
    model = Pic
    template_name = "daisy/pic_detail.html"
    def get(self, request, pk) :
        x = Pic.objects.get(id=pk)
        comments = Comment.objects.filter(pic=x).order_by('-updated_at')
        comment_form = CommentForm()
        context = { 'pic' : x, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)

class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        x = get_object_or_404(Pic, id=pk)
        comment = Comment(comment=request.POST['comment'], owner=request.user, pic=x)
        comment.save()
        return redirect(reverse('daisy:pic_detail', args=[pk]))

class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "daisy/comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        pic = self.object.pic
        return reverse('daisy:pic_detail', args=[pic.id])