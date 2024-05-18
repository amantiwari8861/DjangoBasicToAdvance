from django.urls import path
from . import views
urlpatterns=[
    path("",views.say_hi),
    path("hi/",views.say_hi),
    path("hello/",views.greet_user),
    path("home/",views.index),
    path("add/", views.form_update, name="saveform")
]