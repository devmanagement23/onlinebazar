from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="Blogindex"),
    path("home",views.home,name="BlogHome"),
]
