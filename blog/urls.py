from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name='home'),
    path('upload/', views.UploadPost.as_view(), name='upload_post'),
    path('edit/<slug:slug>', views.EditPost.as_view(), name='edit_post'),
    path('delete/<slug:slug>', views.DeletePost.as_view(), name='delete_post'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('comment/delete/<int:post_id>/', views.DeleteComment.as_view(), name='comment_delete'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('contact/', views.contact, name='contact'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
