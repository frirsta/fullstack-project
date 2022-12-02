from django.urls import path
from .views import HomeView, PostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<primaryKey>/<slug:slug>', PostView.as_view(), name='post')
]
