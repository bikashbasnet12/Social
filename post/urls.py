from django.urls import path
from.views import delete_post_view, edit_post_view
from post.views import create_view

urlpatterns = [
    path('create/',create_view,name = "create"),
    path('delete/<pk>/',delete_post_view,name="delete_post"),
    path('edit/<pk>',edit_post_view,name="edit")
]
