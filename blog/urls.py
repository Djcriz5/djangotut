from django.conf.urls import include, url
from . import views

urlpatterns = [
        url('posts/', views.post_list),
    ]