from django.urls import path

from . import views

app_name = 'public'
urlpatterns = [
    path("", views.index, name="index"),
    path("blog", views.premium, name="blog"),
    path("podcast", views.support, name="podcast"),
    path("events", views.download, name="events"),
    path("about", views.about, name="about")
]
