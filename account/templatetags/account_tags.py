from django import template
register = template.Library()


@register.inclusion_tag('registration/partials/active_navbar.html')
def active_navbar(request, link_name, icon_classes, content):
    return {
        "request":request,
        "link_name":link_name,
        "link":"account:{}".format(link_name),
        "icon_classes": icon_classes,
        "content":content,
    }