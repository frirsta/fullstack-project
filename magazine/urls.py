from django.urls import path
from .views import HomeView, PostView, PostCreateView, PostDeleteView, PostUpdateView, UserPostView, AdminPage, CommentDeleteView, AllPostsView, AdminPostDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('posts/', AllPostsView.as_view(), name='posts'),
    path('post/<pk>/<slug:slug>', PostView.as_view(), name='post'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('users/user-posts/', UserPostView.as_view(), name='user_posts'),
    path('admin-page/', AdminPage.as_view(), name='admin_page'),
    path('<int:pk>/admin-page/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('<int:pk>/admin-page/delete-post/', AdminPostDeleteView.as_view(), name='admin_post_delete'),
]
