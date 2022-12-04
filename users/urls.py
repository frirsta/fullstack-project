from django.urls import path
from . views import signup, loginUser, logoutUser, profile


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('profile/<username>/', profile, name='profile'),
    path('about_user/', about_user, name='about_user'),
]
