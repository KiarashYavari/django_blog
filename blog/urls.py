from django.conf import settings
from django.urls import path
from blog.views import article_exclusive, home
from django.conf.urls.static import static

app_name="blog"
urlpatterns = [
    path('',home, name="home"),
    path('articles/<slug:Slug>',article_exclusive, name="article_exclusive"),
]