from API import views
from django.urls import path

urlpatterns = [
    path('posts/', views.PostListCreateAPIView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', views.PostDetailAPIView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comments/', views.CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path('posts/<int:post_id>/like/', views.LikeCreateAPIView.as_view(), name='like-create'),
    # path('posts/create/', views.PostCreateAPIView.as_view(), name='post-create'),
    path('posts/<int:pk>/update/', views.PostUpdateAPIView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteAPIView.as_view(), name='post-delete'),
    # path('api/token/', views.CustomObtainAuthToken.as_view(), name='api_token_auth'),
    path('register/', views.UserCreateAPIView.as_view(), name='user-register'),
    path('login/', views.CustomObtainAuthToken.as_view(), name='user-login'),

]