from django.conf.urls import url
from api_compressor.views import BookmarkListView, BookmarkDetailView

urlpatterns = [
    url(r'^bookmark/$', BookmarkListView.as_view(), name='api_bookmark_list'),
    url(r'^bookmark/(?P<pk>\d+)/$', BookmarkDetailView.as_view(), name="api_bookmark_detail")
]