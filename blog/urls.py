from django.conf import settings
from django.urls import path
from blog.views import article_exclusive, ArticlesLists, category

app_name="blog"
urlpatterns = [
    path('',ArticlesLists.as_view(), name="home"),
    path('page/<int:page>',ArticlesLists.as_view(), name="home"),
    path('articles/<slug:Slug>',article_exclusive, name="article_exclusive"),
    path('category/<slug:Slug>',category, name="category"),
    path('category/<slug:Slug>/page/<int:page>',category, name="category"),
]