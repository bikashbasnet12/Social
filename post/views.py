from django.shortcuts import redirect, render

from post.forms import createpostform

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