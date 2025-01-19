from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
# -----------------------------------------------------
from django.shortcuts import get_object_or_404, render
from .models import Post
from django.views.generic import ListView
# -----------------------------------------------------
from .forms import UserForm, PostForm

# Create your views here.
def main(request):
    return render(request, 'main.html')

def about(request):
    return render(request, 'about.html')

def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)

def privacy_policy(request):
    return render(request, 'privacyPolicy.html')

def contacts(request):
    return render(request, 'contacts.html')

def tos(request):
    return render(request, 'tos.html')

from django.shortcuts import render, redirect
from .forms import UserForm

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
            return redirect('/')
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = UserForm()
    return render(request, 'reg.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user, password)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 5
    template_name = "blog_list.html"


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, status="published", publish__yead=year, publish__month=month, publish__day=day)
    return render(request, 'blog_detail.html', {'post': post})

def test(request):
    return render(request, 'base.html')

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Установите автора текущим пользователем
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', year=post.publish.year, month=post.publish.month, day=post.publish.day, slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})