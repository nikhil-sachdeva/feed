from django.shortcuts import render
from .models import Post
from django.views import generic

def index(request):
    num_post=Post.objects.all().count()
    num_happy=Post.objects.filter(feel__exact='h').count()
    num_sad=Post.objects.filter(feel__exact='s').count()
    return render(
        request,
        'feed/index.html',
        context={'num_happy':num_happy,'num_sad':num_sad,'num_post':num_post},
    )
class PostView(generic.ListView):
    model=Post

class PostDetailView(generic.DetailView):
    model=Post

# Create your views here.
