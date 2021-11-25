from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Article

# Create your views here.
class ArticlesList(LoginRequiredMixin,ListView):
    queryset = Article.objects.all
    template_name = "registration/home.html"