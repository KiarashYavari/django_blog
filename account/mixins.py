from django.shortcuts import get_object_or_404
from django.http.response import Http404
from django.http import Http404

from blog.models import Article

class FieldAccessMixin():
    """Verify that the current user is authenticated."""
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = ['Title', 'Category', 'Author', 'Description', 'Slug', 'Thumbnail', 'Published', 'Status']
        elif request.user.Is_Author:
            self.fields = ['Title', 'Category', 'Description', 'Slug', 'Thumbnail', 'Published']
        else:
            raise Http404("شما مجاز به مشاهده این صفحه نیستید")
        
        return super().dispatch(request, *args, **kwargs)


class FormValidMixin():
    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.Author = self.request.user
            self.obj.Status = "d"
        return super().form_valid(form)


class UserAccessMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        if article.Author == request.user and article.Status in ["b", "d"]\
            or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs) 
        else:
            raise Http404("شما مجاز به مشاهده این صفحه نیستید")
        

class SuperUserAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("شما مجاز به مشاهده این صفحه نیستید")
               