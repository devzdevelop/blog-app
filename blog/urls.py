from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
    path('post/new/', views.BlogCreateView.as_view(), name='post_new'),
    path('post/<pk>/edit/', views.BlogUpdateView.as_view(), name='post_update'),
    path('post/<pk>/delete', views.BlogDeleteView.as_view(), name='post_delete'),
]
