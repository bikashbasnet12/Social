from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from post.models import post
# Create your views here.
@login_required
def dashboard_view(request):
    posts = post.objects.filter(user = request.user)
    return render(request,'dashboard/dashboardview.html',
                  
                  {
                      "posts":posts
                  }
                  )