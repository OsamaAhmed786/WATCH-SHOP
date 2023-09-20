from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.Startup, name="start"),
    path("home/", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("shop/", views.shop, name="shop"),
    path("item/", views.item, name="single")
    
]
