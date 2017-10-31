from .models import Post, Comment
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import sys

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
