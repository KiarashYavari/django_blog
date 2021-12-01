from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Article

# Create your views here.
class ArticlesList(LoginRequiredMixin,ListView):
    template_name = "registration/home.html"
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all
        else:
            return Article.objects.filter(Author=self.request.user)


class ArticleCreate(LoginRequiredMixin,CreateView):
    model = Article
    template_name = "registration/article_create_update.html"
    fields = ['Title', 'Category', 'Author', 'Description', 'Slug', 'Thumbnail', 'Published', 'Status']
    