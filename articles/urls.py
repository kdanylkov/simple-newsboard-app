from django.urls import path

from articles.views import ArticleCreateView
from articles.views import ArticleDeleteView
from articles.views import ArticleDetailView
from articles.views import ArticleListView
from articles.views import ArticleUpdateView

urlpatterns = [
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('', ArticleListView.as_view(), name='article_list'),
]
