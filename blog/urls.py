from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('test1', views.test1, name='test1.html'),
    path('test2', views.test2, name='test2.html'),
]

