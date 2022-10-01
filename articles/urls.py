from django.urls import path
from .views import PostListView, ArticleUpdateView, ArticleDetailView, ArticleDeleteView, ArticleCreateView


urlpatterns = [
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name = 'article_update'),
    path('<int:pk>/', ArticleDetailView.as_view(), name = 'article_detail'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name = 'article_delete'),
    path('new/', ArticleCreateView.as_view(), name = 'article_new' ),   
    path('', PostListView.as_view(), name='posts'),

]