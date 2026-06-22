from django.urls import path
from .views import PostView, PostCreateView

urlpatterns = [
    path('create/', PostCreateView.as_view()),
    path('post/', PostView.as_view())
]
