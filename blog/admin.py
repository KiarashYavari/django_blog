from django.contrib import admin
from blog.models import Article, Categories
from django.utils.translation import ngettext
from django.contrib import messages

# Register your models here.
@admin.action(description='انتشار مقالات')
def make_published(modeladmin, request, queryset):
    updated=queryset.update(Status='p')
    modeladmin.message_user(request, ngettext(
            '%d  مقاله منتشر شد',
            '%d مقاله منتشر شدند ',
            updated,
        ) % updated, messages.SUCCESS)



@admin.action(description='پیش نویس کردن مقالات')
def make_draft(modeladmin, request, queryset):
    updated=queryset.update(Status='d')
    modeladmin.message_user(request, ngettext(
            '%d  مقاله پیش نویس  شد',
            '%d مقاله پیش نویس  شدند ',
            updated,
        ) % updated, messages.SUCCESS)



admin.site.site_header = "پنل مدیریت وبلاگ"


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('Position','Title', 'Slug', 'Parent','Status')
    list_filter = (['Status'])
    search_fields = ('Title', 'Slug')
    prepopulated_fields = {"Slug": ("Title",)}
    
           
admin.site.register(Categories, CategoriesAdmin)



class ArticleAdmin(admin.ModelAdmin):
    list_display = ('Title', 'thumbnail_tag', 'Author', 'Category_str','Slug', 'publish_time', 'Status')
    list_filter = ('Published', 'Status' ,'Category', 'Author')
    search_fields = ('Title', 'Description')
    prepopulated_fields = {"Slug": ("Title",)}
    ordering = ('-Status', '-Published')
    actions = [make_published, make_draft]
    
    def Category_str(self,cat_obj):
        return "، ".join([Category.Title for Category in cat_obj.Category.published()])
    Category_str.short_description = "دسته بندی ها"
    
        
admin.site.register(Article, ArticleAdmin)
