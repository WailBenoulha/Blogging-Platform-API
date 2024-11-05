from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import ArticleView,UserView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('Article/',ArticleView.as_view(),name='Article'),
    path('Article/<int:pk>/',ArticleView.as_view(),name='Article-detail'),
    path('user/',UserView.as_view(),name='user'),
]