from django.conf import settings
from django.urls import path
from blog.views import ArticleDetail, ArticlesLists, CategoryList, AuthorList, ArticlePreview

app_name="blog"
urlpatterns = [
    path('',ArticlesLists.as_view(), name="home"),
    path('page/<int:page>',ArticlesLists.as_view(), name="home"),
    path('articles/<slug:Slug>',ArticleDetail.as_view(), name="ArticleDetail"),
    path('preview/<int:pk>',ArticlePreview.as_view(), name="ArticlePreview"),
    path('category/<slug:Slug>',CategoryList.as_view(), name="category"),
    path('category/<slug:Slug>/page/<int:page>',CategoryList.as_view(), name="category"),
    path('author/<slug:username>',AuthorList.as_view(), name="author"),
    path('author/<slug:username>/page/<int:page>',AuthorList.as_view(), name="author"),
]