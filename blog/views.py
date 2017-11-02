from .models import Post, Comment
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate


import sys
from django.http import HttpResponse

def main_page(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/index.html', {'posts': posts})

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'Post':
        text = request.POST['comment_text']
        user = request.user

        comment = Comment(author = user, text = text, post = post)
        comment.save()

    return render(request, 'blog/index.html', {
        'post': post
    })

@login_required
def home(request):
    return render(request, 'blog/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('http://dmytrolutchyn.pythonanywhere.com')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})