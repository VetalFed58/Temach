from .models import Post, Comment
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from datetime import datetime
from django.contrib.auth.models import User

def main_page(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/index.html', {'posts': posts})

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        text = request.POST['comment_text']
        user = request.user

        comment = Comment(author = user, text = text, post = post)
        comment.save()
        return redirect('/')

    return render(request, 'blog/index.html', {
        'post': post
    })

def load_new_fixtures(request):
    table = []
    if request.method == 'POST':
        text = request.POST['fixtures']
        for line in text.splitlines():
            team1, score, team2, year, month, link = line.split(',')
            author = User.objects.get(pk=1)
            text = '''
                <p><a href="{link}">See more info</a></p>
            '''.format(
                link = link
            )
            post = Post(title = team1 + score + team2, text =text, author = author, published_date = datetime.now())
            post.save()
            table.append([team1, score, team2, year, month, link])
    return render(request, 'blog/table.html', {
        "table": table
    })

@login_required
def home(request):
    return render(request, 'blog/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('http://dmytrolutchyn.pythonanywhere.com')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})




