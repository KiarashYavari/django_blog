from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import FieldAccessMixin, FormValidMixin, UserAccessMixin, SuperUserAccessMixin
from blog.models import Article
from .models import User
from .forms import ProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

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


class ArticleDelete(SuperUserAccessMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('account:home')
    template_name = 'registration/article_confirm_delete.html'


class UserProfile(LoginRequiredMixin,UpdateView):
    model = User
    template_name = "registration/profile.html"
    form_class = ProfileForm
    # fields = ['first_name', 'last_name', 'username', 'Is_Author', 'Special_User']
    success_url = reverse_lazy("account:profile")

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

    
    def get_form_kwargs(self):
        kwargs = super(UserProfile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user,
        })
        return kwargs



class Login(LoginView):
    def get_success_url(self):
        user = self.request.user
        if user.is_superuser or user.Is_Author:
            return reverse_lazy("account:home")
        else:
            return reverse_lazy("account:profile")