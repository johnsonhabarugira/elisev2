from django.shortcuts import render,get_object_or_404
from blog.models import Post, Comment
from .forms import CommentForm

# Create your views here.

def gettingblog(request):
    blogpost= Post.objects.order_by('-created_at')[:20]
    recentpost = Post.objects.order_by('-created_at')[:5]
    context = {
        'blogpost': blogpost,
        'recentpost': recentpost,
    }
    return render(request, 'blog/blogs.html', context)

def oneblog(request, pk):
    viewpost = Post.objects.select_related('author').get(id=pk)
    commentsv = Comment.objects.filter(post=pk)
    comment_count = Comment.objects.filter(post=pk).count()
    post = get_object_or_404(Post, id=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            viewpost = Post.objects.select_related('author').get(id=pk)
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            context = {
        'viewpost': viewpost,
        'commentsv':commentsv,
        'comment_count':comment_count,
        'form': form,
    }
            return render(request, 'blog/blog-details.html', context)
    else:
        form = CommentForm()

    context = {
        'viewpost': viewpost,
        'commentsv':commentsv,
        'comment_count':comment_count,
        'form': form,
    }
    return render(request, 'blog/blog-details.html', context)
