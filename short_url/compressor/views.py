from django.contrib.auth import forms, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, View, DetailView, CreateView, UpdateView, DeleteView
from compressor.forms.forms import UserForm
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
        if request.user.id:
            Click.objects.create(clicker=request.user, bookmark=bookmark)
        else:
            Click.objects.create(bookmark=bookmark)
        return HttpResponseRedirect(bookmark.long_url)

    def get(self, request, bookmark_id):
        bookmark = Bookmark.objects.get(short_url=bookmark_id)
        return HttpResponseRedirect(bookmark.long_url)

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields =  ["title", "description"]
    success_url = '/'

    def get_queryset(self):
        bookmark_id = self.kwargs.get("pk")
        return self.model.objects.filter(id=bookmark_id)

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = '/'

class RedirectView(View):

    def get(self, request, shortend_url):
        bookmark = Bookmark.objects.get(short_url=shortend_url)
        return HttpResponseRedirect(bookmark.long_url)

class SignupUser(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/'

def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(new_user)
            # redirect, or however you want to get to the main view
            return HttpResponseRedirect('/')
    else:
        form = UserForm()

    return render(request, 'auth/user_form.html', {'form': form})

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print( user_form.errors)
    else:
        user_form = UserForm()
    return render(request,
            'auth/user_form.html',
            {'user_form': user_form,
            'registered': registered})