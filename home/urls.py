from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name="index"),
    path('mannschaften/', views.mannschaften, name="mannschaften"),
    path('mannschaften/<str:mannschaft>', views.mannschaft, name="mannschaft"),
    path('training/', views.training, name="training")
]
