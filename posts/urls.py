from posts import views
from django.urls import path
from .views import post_new

urlpatterns = [
    path('', views.PostList.as_view(), name='posts'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('', post_new, name='post_new'),
]
