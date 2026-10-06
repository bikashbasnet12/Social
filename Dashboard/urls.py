from django.urls import path

from Dashboard.views import dashboard_view
urlpatterns = [
    path('',dashboard_view,name="dashboard")
]
