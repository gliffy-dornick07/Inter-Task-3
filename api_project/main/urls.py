from django.urls import path
from .views import (
    RegisterView,
    AuthorListCreateView,
    AuthorRetrieveUpdateDestroyView,
    ArticleListCreateView,
    ArticleRetrieveUpdateDestroyView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Authentication Endpoints
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Author Endpoints
    path('authors/', AuthorListCreateView.as_view(), name='author_list_create'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroyView.as_view(), name='author_detail'),

    # Article Endpoints
    path('articles/', ArticleListCreateView.as_view(), name='article_list_create'),
    path('articles/<int:pk>/', ArticleRetrieveUpdateDestroyView.as_view(), name='article_detail'),
]
