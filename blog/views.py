from django.shortcuts import render,get_object_or_404
from blog.models import Article, Categories


# Create your views here.
def home(request):
    context = {
        "articles": Article.objects.filter(Status = 'p'),
        "categories": Categories.objects.filter(Status = True),
    }
    return render(request, 'home.html', context)


def article_exclusive(request, Slug):
    context = {
        "article": get_object_or_404(Article, Slug = Slug, Status = 'p')
    }
    return render(request, 'article_exclusive.html', context)

    
    
