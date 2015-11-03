from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.serializers import ModelSerializer
from compressor.models import Bookmark


class BookmarkSerializer(ModelSerializer):

    class Meta:
        model = Bookmark


class BookmarkListView(ListCreateAPIView):
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()

class BookmarkDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()