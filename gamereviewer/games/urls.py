from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    )


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
    path('create-game/', views.create_game, name='create-game'),
    path('game_list/', views.game_list, name='game-lists'),
    path('games/<int:pk>/', views.game_detail, name='game-detail'),
    path('reviews/', views.review_list, name='review-list'),
    path('reviews/create/', views.create_review, name='create-review'),
    path('reviews/<int:pk>/', views.review_detail, name='review-detail'),
    path('comments/', views.comment_list, name='comment-list'),
    path('comments/create/', views.create_comment, name='create-comment'),
    
]
#path('comments/', views.CommentList.as_view(), name='comment-list'),
#URL pattern for the root path,
#path('', views.index, name='index'),
#path('games/', views.GameList.as_view(), name='game-list'),
# path('api/user/',views.UserAPIView.as_view(), name='user'),