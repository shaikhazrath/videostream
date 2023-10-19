from django.urls import path
from . import views

app_name = 'videostreamingapp'

urlpatterns = [
    path('',views.home,name='index'),
    path('video/<int:id>', views.video, name='index'),
    path('stream_video/<int:id>', views.stream_video, name='stream_video'),
]
