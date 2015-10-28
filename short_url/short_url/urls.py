"""short_url URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from compressor.views import default_view, BookmarkListView, BookmarkCreateView, BookmarkDetailView, \
    UserBookmarkListView, ClickView, BookmarkUpdateView, BookmarkDeleteView, RedirectView, SignupUser, add_user, \
    register

urlpatterns = [
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', BookmarkListView.as_view(), name='bookmark_list'),
    url(r'^create/$', login_required(BookmarkCreateView.as_view()), name="bookmark_create"),
    url(r'^bookmark/(?P<pk>\d+)$', BookmarkDetailView.as_view(), name="bookmark_detail"),
    url(r'^user/(?P<pk>\d+)$', UserBookmarkListView.as_view(), name="user_bookmark_list"),
    url(r'click/(?P<bookmark_id>\d+)/$', ClickView.as_view(), name="click"),
    url(r'^update/(?P<pk>\d+)$', login_required(BookmarkUpdateView.as_view()), name="bookmark_update"),
    url(r'^delete/(?P<pk>\d+)$', login_required(BookmarkDeleteView.as_view()), name="bookmark_delete "),
    url(r'^zach/(?P<bookmark_id>\w+)$', ClickView.as_view(), name="redirect"),
    url(r'^user_create/$', SignupUser.as_view(), name='signup')
]
