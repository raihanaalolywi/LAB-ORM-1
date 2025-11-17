from . import views
from django.urls import path

app_name = "main"


urlpatterns = [
    path("", views.home_view, name="home_view"),                   # عرض المنشورات
    path("add/", views.add_post_view, name="add_post_view"),       # إضافة منشور

    path("post/<int:post_id>/", views.post_detail_view, name="post_detail_view"),  # تفاصيل

    path("post/<int:post_id>/edit/", views.edit_post_view, name="edit_post_view"), # تعديل

    path("post/<int:post_id>/delete/", views.delete_post_view, name="delete_post_view"), # حذف
]

