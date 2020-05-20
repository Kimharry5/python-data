from django.conf.urls import url
from api.views import index_views


urlpatterns = [
    url('index/$', index_views.index, name='index'),
]
