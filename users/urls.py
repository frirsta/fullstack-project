from django.urls import path, reverse_lazy
from . views import signup, loginUser, logoutUser, profile, AboutMeForm, edit_user_profile
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('profile/<username>/', profile, name='profile'),
    path('about_user/', edit_user_profile, name='about_user'),
    path('password_change/', PasswordChangeView.as_view(
        template_name='users/password_change.html',
        success_url=reverse_lazy('users:password_change_done')),
        name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(
        template_name='users/password_change_done.html'),
        name='password_change_done'),
]
