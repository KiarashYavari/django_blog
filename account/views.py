from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import FieldAccessMixin, FormValidMixin, UserAccessMixin
from blog.models import Article

# Create your views here.
class ArticlesList(LoginRequiredMixin,ListView):
    template_name = "registration/home.html"
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all
        else:
            return Article.objects.filter(Author=self.request.user)


class ArticleCreate(LoginRequiredMixin, FieldAccessMixin, FormValidMixin, CreateView):
    model = Article
    template_name = "registration/article_create_update.html"


class ArticleUpdate(UserAccessMixin, FieldAccessMixin, FormValidMixin, UpdateView):
    model = Article
    template_name = "registration/article_create_update.html"
    