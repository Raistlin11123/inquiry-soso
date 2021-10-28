from . import views
from django.urls import path

urlpatterns = [
    #Maybe a generic view?
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'), #1 = historic, ...
    path('logout/', views.logout_view, name='logout')
]