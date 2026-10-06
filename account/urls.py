from django.urls import path

from account.views import login_view, register_view, user_profile

urlpatterns = [
    path('register/',register_view,name="register_user"),
    path('login/',login_view,name= "login_user"),
    path('user/<username>',user_profile,name ="user_profile")
]
