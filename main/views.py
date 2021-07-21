from django.shortcuts import redirect, render,get_object_or_404, redirect
from .models import Post, Comment
from django.utils import timezone

def showmain(request):
    posts = Post.objects.all()
    return render(request, 'main/mainpage.html',{'posts':posts})

def childhood(request):
    return render(request, 'main/childhood.html')

def teenager(request):
    return render(request, 'main/teenager.html')

def adult(request):
    return render(request, 'main/adult.html')

def posts(request):
    posts = Post.objects.all()
    return render(request, 'main/posts.html',{'posts':posts})

def detail(request,id):
    post=get_object_or_404(Post, pk =id)
    all_comments=post.comments.all().order_by('-created_at')
    return render(request,'main/detail.html',{'post':post, 'comments':all_comments})

def new(request):
    return render(request, 'main/new.html')

def create(request):              #데이터 베이스에 데이터를 저장하는 create 함수
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.user
    new_post.pub_date = timezone.now()
    new_post.image= request.FILES.get('image')
    new_post.body = request.POST['body']
    new_post.save()
    return redirect('main:detail',new_post.id)

def edit(request, id):
    edit_post = Post.objects.get(id = id)
    return render(request, 'main/edit.html',{'post' :edit_post})

# Create your views here.
def update(request, id):
    update_post= Post.objects.get(id=id)
    update_post.title = request.POST['title']
    update_post.writer = request.user
    update_post.pub_date = timezone.now()
    update_post.image= request.FILES.get('image')
    update_post.body = request.POST['body']
    update_post.save()
    return redirect('main:detail', update_post.id)

def delete(request, id):
    delete_post = Post.objects.get(id = id)
    delete_post.delete()
    return redirect('main:posts')

def create_comment(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=post_id)
        current_user=request.user
        comment_content=request.POST.get('content')
        Comment.objects.create(content=comment_content, writer=current_user, post=post)
    return redirect('main:detail', post_id)


    