from django.urls import path
from home import views

urlpatterns = [
    path('',views.IndexPageView.as_view(),name="index"),
    path('author/<int:pk>',views.UserDetailView.as_view(),name="author_detail"),
    path('authors/',views.UserListView.as_view(),name="author_list"),
    path('post/<int:pk>',views.PostDetailView.as_view(),name="post_detail"),
    path('posts/',views.PostListView.as_view(),name="post_list"),
]