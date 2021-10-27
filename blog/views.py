from django.core import paginator
from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404
from blog.models import Article, Categories


# Create your views here.
def home(request,page=1):
    articles_list = Article.objects.filter(Status = 'p')
    paginator = Paginator(articles_list, 5)
    context = {
        "articles": paginator.get_page(page)
    }
    return render(request, 'home.html', context)


def article_exclusive(request, Slug):
    context = {
        "article": get_object_or_404(Article, Slug = Slug, Status = 'p')
    }
    return render(request, 'article_exclusive.html', context)


def category(request, Slug, page=1):
    category_list = get_object_or_404(Categories, Slug = Slug, Status = True)
    article_list = category_list.articles.published()
    paginator = Paginator(article_list, 5)

    context ={
        'category': category_list,
        'articles': paginator.get_page(page),
    }
    return render(request, 'category.html', context)
    
