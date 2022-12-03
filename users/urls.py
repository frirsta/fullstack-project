from django.urls import path
from . views import signup, loginUser


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', loginUser, name='login'),
]
