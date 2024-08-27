from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.loginview),
    path('logout/',views.logoutView),
]