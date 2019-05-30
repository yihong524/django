from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.HomeListView.as_view(), name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path('log/', views.log_message, name="log"),
]