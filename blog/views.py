from account.models import User
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from blog.models import Article, Categories
from account.mixins import UserAccessMixin


# Create your views here.

class ArticlesLists(ListView):
    queryset = Article.objects.published()
    context_object_name = 'articles'
    template_name = 'blog/articles_lists.html'
    paginate_by = 5



class ArticleDetail(DetailView):
    template_name = 'blog/article_detail.html'

    def get_object(self):
        Slug = self.kwargs.get('Slug')
        return get_object_or_404(Article.objects.published(), Slug = Slug)


class ArticlePreview(UserAccessMixin, DetailView):
    template_name = 'blog/article_detail.html'

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Article, pk = pk)


class CategoryList(ListView):
    paginate_by = 5
    template_name = 'blog/category_list.html'

    def get_queryset(self):  # get category object and return articles categorize by that category
        global category
        Slug = self.kwargs.get('Slug')
        self.category = get_object_or_404(Categories, Slug = Slug, Status = True)
        return self.category.articles.published()
    
    def get_context_data(self, **kwargs): # manipulate contextes and set category context value
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context



class AuthorList(ListView):
    paginate_by = 5
    template_name = 'blog/author_list.html'

    def get_queryset(self):  # get author object and return articles grouped by that author
        username = self.kwargs.get('username')
        self.author = get_object_or_404(User, username=username)
        return self.author.articles.published()
    
    def get_context_data(self, **kwargs): # manipulate contextes and set author context value
        context = super().get_context_data(**kwargs)
        context['author'] = self.author
        return context
