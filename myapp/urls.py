from django.urls import path
from . import views

urlpatterns = [
    path('app1/', views.home, name="home"),
    path('app1/profile/<str:name>/<int:age>/', views.show_profile, name='profile'),
]