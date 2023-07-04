from django.contrib import admin
from django.urls import path
from events import views


urlpatterns = [
    path('', views.display_events, name="display_events"),
    path('create_event/', views.create_event,name="create_event"),
    path('my_events/', views.my_events, name="my_events"),

]