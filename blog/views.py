from django.shortcuts import render
from blog.models import Post
from django.utils import timezone


# Create your views here.
def post_list(request):
    postsqueryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': postsqueryset})
