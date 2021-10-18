from django.contrib import admin
from django.utils import timezone
from blog.models import Article, Categories

# Register your models here.
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('Position','Title', 'Slug','Status')
    list_filter = (['Status'])
    search_fields = ('Title', 'Slug')
    prepopulated_fields = {"Slug": ("Title",)}
    
           
admin.site.register(Categories, CategoriesAdmin)



class ArticleAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Category_str','Slug', 'publish_time', 'Status')
    list_filter = ('Published', 'Status' ,'Category')
    search_fields = ('Title', 'Description')
    prepopulated_fields = {"Slug": ("Title",)}
    ordering = ('-Status', '-Published')
    
    def Category_str(self,cat_obj):
        return "، ".join([Category.Title for Category in cat_obj.Category.all()])
    Category_str.short_description = "دسته بندی ها"
    
        
admin.site.register(Article, ArticleAdmin)
