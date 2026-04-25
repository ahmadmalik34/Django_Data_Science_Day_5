from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, PostForm
from blog.models import Post, Author

# ========== AUTHENTICATION VIEWS ==========

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now login.')
            return redirect('accounts:login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
    else:
        form = RegisterForm()
    
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('accounts:profile')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('blog:post_list')


@login_required(login_url='accounts:login')
def profile(request):
    user = request.user
    # Get or create author for this user
    author, created = Author.objects.get_or_create(
        user=user,
        defaults={'name': user.get_full_name() or user.username, 'email': user.email}
    )
    posts = Post.objects.filter(author=author).order_by('-created_at')
    
    context = {
        'user': user,
        'author': author,
        'posts': posts,
        'post_count': posts.count(),
    }
    return render(request, 'accounts/profile.html', context)


@login_required(login_url='accounts:login')
def create_post(request):
    user = request.user
    author, created = Author.objects.get_or_create(
        user=user,
        defaults={'name': user.get_full_name() or user.username, 'email': user.email}
    )
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = author
            post.save()
            form.save_m2m()
            messages.success(request, 'Post created successfully!')
            return redirect('accounts:profile')
    else:
        form = PostForm()
    
    return render(request, 'accounts/create_post.html', {'form': form})


@login_required(login_url='accounts:login')
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)
    
    # Check if user owns this post
    if post.author.user != request.user:
        messages.error(request, 'You can only edit your own posts.')
        return redirect('accounts:profile')
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('accounts:profile')
    else:
        form = PostForm(instance=post)
    
    return render(request, 'accounts/edit_post.html', {'form': form, 'post': post})


@login_required(login_url='accounts:login')
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    
    # Check if user owns this post
    if post.author.user != request.user:
        messages.error(request, 'You can only delete your own posts.')
        return redirect('accounts:profile')
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('accounts:profile')
    
    return render(request, 'accounts/delete_post.html', {'post': post})