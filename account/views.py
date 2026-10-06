from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from account.forms import LoginUserForm, RegisteruserForm
# Create your views here.
from django.contrib.auth import get_user_model,login,authenticate

from post.models import post
User = get_user_model()

def register_view(request):
    if request.method == "POST":
        form = RegisteruserForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username = form.cleaned_data.get("username")).exists():
                form.add_error("username", "Username already exists"
                )
            elif User.objects.filter(email = form.cleaned_data.get("email")).exists():
                form.add_error("email", "Email already exists")

            else:
                User.objects.create_user(**form.cleaned_data)
                return redirect("login_user")
    else:
        form = RegisteruserForm()

    return render(request, 'account/register.html', {
        "form": form
    })

def login_view(request):
    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            user  = authenticate(request,**form.cleaned_data)
            if user:
                login(request,user)
                return redirect("dashboard")
            form.add_error(None,"username or password invalid")
    else:
     form = LoginUserForm()

    return render(request, 'account/login.html', {
        "form": form
    })

def user_profile(request,username):
    user = get_object_or_404(User,username= username)
    if user:
        posts = post.objects.filter(user=user)

    return render(request,"account/profile.html",{
        "user":user,
        "posts":posts

    })
