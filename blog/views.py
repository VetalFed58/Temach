from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from datetime import datetime
from django.contrib.auth.models import User

from django.utils import timezone
import sched, time

def main_page(request):
    page = request.GET.get('page', 1)
    paginator = Paginator(Post.objects.all()[::-1], 20)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/index.html', {'posts': posts})

def userposts_page(request):
    page = request.GET.get('page', 1)
    paginator = Paginator(Post.objects.filter(topic="user")[::-1], 20)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/index.html', {'posts': posts})

def football_page(request):
    page = request.GET.get('page', 1)
    paginator = Paginator(Post.objects.filter(topic="football")[::-1], 20)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/index.html', {'posts': posts})

def technologies_page(request):
    page = request.GET.get('page', 1)
    paginator = Paginator(Post.objects.filter(topic="technologies")[::-1], 20)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/index.html', {'posts': posts})

def post(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=post_id)
        if request.method == 'POST':
            text = request.POST['comment_text']
            user = request.user
            comment = Comment(author = user, text = text, post = post)
            comment.save()
            return redirect('/')
    else:
        return redirect('/login/')
    return render(request, 'blog/index.html', {
        'post': post
    })

def load_new_fixtures(request):
    table = []
    if request.method == 'POST':
        text = request.POST['fixtures']
        for line in text.splitlines():
            team1, score, team2, year, month, link = line.split(',')
            author = User.objects.all()[12]
            text = '''
                <p>{0} {1} {2}. <a href="{3}">See more info</a></p>
            '''.format(team1,score,team2,link)
            post = Post(topic = "football", text =text, author = author, published_date = datetime.now())
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
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def create_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            text = request.POST['text']
            date = datetime.now()
            author = request.user
            post = Post(topic = 'user', text = text, author = author, published_date = date)
            post.save()
            return redirect('/')
    else:
        return redirect('/login/')
    return render(request, 'blog/create_post.html', {})