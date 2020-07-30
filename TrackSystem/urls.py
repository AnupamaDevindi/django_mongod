from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    #url(r'^$', views.track_list, name='track_list'),
    url(r'^api/TrackSystem$', views.track_list)
]
