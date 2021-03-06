from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from .forms import PostForm, CommentForm
from .models import Post, Category, Comment
from rest_framework.views import APIView
from .serializer import PostSerializer


def home(request):
    posts = Post.objects.all
    categories = Category.objects.all
    form = PostForm
    try:
        last_post = Post.objects.last()
        context = {
            'posts': posts,
            'last_post': last_post,
            'categories': categories,
            'form': form
        }
    except LookupError:
        context = {
            'posts': posts,

            'categories': categories,
            'form': form
        }
    return render(request, 'post/home.html', context)


def add_post(request):
    if request.method == 'POST':
        post = Post()
        post.author = request.user
        post.title = request.POST.get('title')
        post.text = request.POST.get('text')
        post.image = request.FILES.get('image')

        post.category = Category.objects.get(pk=request.POST.get('category'))
        post.save()
    return redirect('/')


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {'post': post, 'comment_form': CommentForm, 'comments_list': Comment.objects.all()}
    return render(request, 'post/post_detail.html', context)


def add_comment(request, slug):
    print(request)
    post = get_object_or_404(Post, slug=slug)
    comment = Comment()
    if request.method == 'POST':
        comment.post = post
        comment.text = request.POST.get('text')
        comment.author = request.user
        comment.save()
    return redirect('post_detail', slug=slug)


class PostApiView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response({"posts": serializer.data})

    def post(self, request):
        post = request.data.get("post")
        serializer = PostSerializer(data=post)
        if serializer.is_valid(raise_exception=True):
            post_save = serializer.save()
        return Response({"success": "Post '{}' created successfully".format(post_save.title)})

