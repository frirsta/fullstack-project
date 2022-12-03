from django.urls import path
from . views import signup, loginUser, logoutUser


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
]
