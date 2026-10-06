from django.urls import path
from post.views import create_view

urlpatterns = [
    path('create/',create_view,name = "create")
]
