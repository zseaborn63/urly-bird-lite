from django.conf.urls import url, include
from api_compressor.views import BookmarkListView, BookmarkDetailView

urlpatterns = [
    url(r'^bookmark/$', BookmarkListView.as_view(), name='api_bookmark_list'),
    url(r'^bookmark/(?P<pk>\d+)/$', BookmarkDetailView.as_view(), name="api_bookmark_detail"),
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
]