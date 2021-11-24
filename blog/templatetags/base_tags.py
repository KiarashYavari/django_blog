from django import template
from ..models import Categories
register = template.Library()

@register.simple_tag
def set_title(data = 'وبلاگ ورزشی'):
    return data


@register.inclusion_tag('blog/partials/category_navbar.html')
def category_navbar():
    context = {
        "categories": Categories.objects.filter(Status = True),
    }
    return context