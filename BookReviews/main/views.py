from django.shortcuts import render, redirect, get_object_or_404
from .models import Post


# الصفحة الرئيسية: عرض المنشورات

def home_view(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, "main/index.html", {"posts": posts})

# صفحة إضافة منشور

def add_post_view(request):

    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        image = request.FILES.get("image")

        Post.objects.create(
            title=title,
            content=content,
            image=image
        )

        return redirect("main:home_view")

    return render(request, "main/add.html")



# صفحة تفاصيل المنشور
def post_detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "main/detail.html", {"post": post})



# صفحة تعديل المنشور

def edit_post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]

        if request.FILES.get("image"):
            post.image = request.FILES["image"]

        post.save()
        return redirect("main:post_detail_view", post_id=post.id)

    return render(request, "main/edit.html", {"post": post})

# حذف منشور (بدون صفحة تأكيد)

def delete_post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect("main:home_view") # هنا انا خليت الحذف كزر action  بدلا ان تكون له صفحة 
