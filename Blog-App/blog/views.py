from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'title':'Zen of Python'
    }
    return render(request, 'blog/home.html', context)

# @login_required is to check if user is logged in, else redirects to login

@login_required
def create_post(request):
    if request.method == 'GET':
        context = {'form': PostForm()}
        return render(request, 'blog/post_form.html', context)
    
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.author=request.user
            user.save()
            messages.success(request,'Post created successfully. ')
            return redirect('posts')
        else:
            messages.error(request,'Correct the following errors: ')
            return render(request, 'blog/post_form.html', {'form': form})

@login_required 
def edit_form(request,id):
    # queryset here is used to retrieve the current users Post objects and matching with
    #  the selected post's id. used to check if the current user is the author of the selected post, if yes
    # then proceed to edit the post else 404 error message
    queryset=Post.objects.filter(author=request.user)
    post=get_object_or_404(queryset,id=id)
    if request.method=='GET':
        context={'form':PostForm(instance=post),'id':id}
        return render(request,'blog/post_form.html',context)
    elif request.method=="POST":
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,'form is updated.')
            return redirect('posts')
        else:
            messages.error(request,' correct the following errors.')
            render(request,'post/post_form.html',{'form':form})

@login_required
def delete_post(request,id):
    # queryset used for same reasons as edit_post() , here its for delete_post
    queryset=Post.objects.filter(author=request.user)
    post=get_object_or_404(queryset,pk=id)
    context={'post':post}
    if request.method=='GET':
        return render(request,'blog/post_confirm_delete.html',context)
    elif request.method=='POST':
        post.delete()
        messages.success(request,'post deleted successfully.')
        return redirect('posts')
    
def about(request):
    return render(request, 'blog/about.html')


