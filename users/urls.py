from django.urls import path
from . views import signup, loginUser, logoutUser, profile, AboutMeForm, edit_user_profile


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('profile/<username>/', profile, name='profile'),
    path('about_user/', edit_user_profile, name='about_user'),
]
