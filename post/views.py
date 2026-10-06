from django.shortcuts import get_object_or_404, redirect, render

from post.forms import createpostform
from post.models import post

# Create your views here.
def create_view(request):
    if request.method == 'POST':
        post_form = createpostform(request.POST,request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit = False)
            post.user = request.user
            post.save()
            return redirect("dashboard")
       
    else: 
     post_form = createpostform()
    return render(request,'post/create_post.html',{

        "form":post_form
    })

def delete_post_view(request,pk):
    post_id = get_object_or_404(post,pk=pk,user = request.user)
    post_id.delete()
    return redirect('user_profile',username = request.user.username)

def edit_post_view(request,pk):
   post_1= get_object_or_404(post,pk=pk,user = request.user)
   if request.method == 'POST':
       form = createpostform(request.POST,request.FILES,instance=post_1)
       if form.is_valid():
          form.save()
          return redirect('user_profile',username =request.user.username)

   else:
    form= createpostform(instance=post_1)
   return render(request,'post/create_post.html',{

      "title":"Edit your Post",
      "form":form
   })