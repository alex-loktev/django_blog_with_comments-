from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from .models import *
from .forms import *

# Create your views here.

class PostList(ListView):
    model = Post
    paginate_by = 3

class PostDetail(View):
    def get(self, request, pk):
        post = Post.objects.get(pk = pk)
        form = CommentForm()
        return render(request, 'blog/post_detail.html', {'post': post, 'form': form})

    def post(self, request, pk):
        post = Post.objects.get(pk = pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect('PostDetail', pk = pk)
        return render(request, 'blog/post_detail.html', {'post': post, 'form': form})

class TagsList(ListView):
    model = Tags
    paginated_by = 3

class TagsDetail(DetailView):
    model = Tags
