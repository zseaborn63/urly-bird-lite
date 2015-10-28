from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, View, DetailView, CreateView, UpdateView, DeleteView
from compressor.models import Bookmark, Click
from hashlib import md5


def default_view(request):
    return HttpResponse("Site working")


class BookmarkListView(ListView):
    model = Bookmark

class BookmarkDetailView(DetailView):
    model = Bookmark

class UserBookmarkListView(ListView):
    model = Bookmark

    def get_queryset(self):
        user_id = self.kwargs.get("pk")
        return self.model.objects.filter(author__id=user_id)

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ["long_url", "description", "title" ]
    success_url = "/"

    def form_valid(self, form):
        model = form.save(commit=False)
        model.author = self.request.user
        _coded_url = bytes(form.instance.long_url, 'utf8')
        m = md5(_coded_url)
        _short_code = m.hexdigest()
        form.instance.short_url = "hpz" + _short_code[:7]
        model.short_url = form.instance.short_url
        return super().form_valid(form)

class ClickView(View):

    def post(self, request, bookmark_id):
        bookmark = Bookmark.objects.get(id=bookmark_id)
        Click.objects.create(clicker=request.user, bookmark=bookmark)
        return HttpResponseRedirect(bookmark.long_url)

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields =  ["title", "description"]

    def get_queryset(self):
        bookmark_id = self.kwargs.get("pk")
        return self.model.objects.filter(id=bookmark_id)

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = '/'

class RedirectView(View):

    def post(self, request, shortend_url):
        _bookmark = Bookmark.objects.get(short_url=shortend_url)
        long_url = _bookmark.long_url
        return HttpResponseRedirect(long_url)
