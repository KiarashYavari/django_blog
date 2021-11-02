from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404
from blog.models import Article, Categories


# Create your views here.
# def home(request,page=1):
#     articles_list = Article.objects.filter(Status = 'p')
#     paginator = Paginator(articles_list, 5)
#     context = {
#         "articles": paginator.get_page(page)
#     }
#     return render(request, 'home.html', context)
class ArticlesLists(ListView):
    queryset = Article.objects.published()
    context_object_name = 'articles'
    template_name = 'home.html'
    paginate_by = 5



# def article_exclusive(request, Slug):
#     context = {
#         "article": get_object_or_404(Article, Slug = Slug, Status = 'p')
#     }
#     return render(request, 'article_exclusive.html', context)
class ArticleDetail(DetailView):
    template_name = 'article_detail.html'

    def get_object(self):
        Slug = self.kwargs.get('Slug')
        return get_object_or_404(Article.objects.published(), Slug = Slug)


# def category(request, Slug, page=1):
#     category_list = get_object_or_404(Categories, Slug = Slug, Status = True)
#     article_list = category_list.articles.published()
#     paginator = Paginator(article_list, 5)

#     context ={
#         'category': category_list,
#         'articles': paginator.get_page(page),
#     }
#     return render(request, 'category.html', context)
class CategoryList(ListView):
    paginate_by = 5
    template_name = 'category_list.html'

    def get_queryset(self):  # get category object and return articles categorize by that category
        global category
        Slug = self.kwargs.get('Slug')
        self.category = get_object_or_404(Categories, Slug = Slug, Status = True)
        return self.category.articles.published()
    
    def get_context_data(self, **kwargs): # manipulate contextes and set category context value
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context
    
