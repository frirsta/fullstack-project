from django.urls import path
from .views import HomeView, PostView, PostCreateView, PostDeleteView, PostUpdateView, UserPostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<pk>/<slug:slug>', PostView.as_view(), name='post'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('users/user-posts/', UserPostView.as_view(), name='user_posts'),
]
