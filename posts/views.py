from django.shortcuts import render, redirect
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from .models import Post
from .forms import PostForm


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'posts/index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'posts/post_detail.html'


# def post_create_view(request):
#     form = PostForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#
#     context = {'form': form}
#
#     return render(
#         request=request,
#         template_name="posts/post_form.html",
#         context=context,
#     )

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            messages.success(request, "New post added.")
            return redirect('posts/post_detail.html', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'posts/post_edit.html', {'form': form})
