from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, View, DetailView, CreateView
from compressor.models import Bookmark


def default_view(request):
    return HttpResponse("Site working")


class BookmarkListView(ListView):
    model = Bookmark

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ["long_url" ]

    def form_valid(self, form):
        model = form.save(commit=False)
        model.author = self.request.user
        return super().form_valid(form)