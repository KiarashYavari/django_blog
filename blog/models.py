from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.html import format_html
from extensions.persian_datetime import persian_calender_datetime


# published article manager:
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(Status='p')

# published category manager
class CategoryManager(models.Manager):
    def published(self):
        return self.filter(Status=True)

class Categories(models.Model):
    Title = models.CharField(max_length=200, verbose_name="عنوان دسته بندی")
    Slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس مخصوص دسته بندی")
    Position = models.IntegerField(verbose_name="جایگاه")
    Status = models.BooleanField(default=1, verbose_name="آیا منتشر شود؟")
    Parent = models.ForeignKey('self', default=None, null=True, blank = True, on_delete=models.SET_NULL, related_name='children', verbose_name='زیر دسته')
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ["Parent__id","Position"]
    def __str__(self):
        return self.Title

    objects = CategoryManager() # change the default manager to custom one
    

class Article(models.Model):
    STATUS_CHOICES = (
        ('p','منتشر شده'),
        ('d','پیش نویس')
    )
    
    Title = models.CharField(max_length=200, verbose_name="عنوان")
    Category = models.ManyToManyField(Categories, verbose_name="دسته بندی", related_name= 'articles')
    Author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='articles', verbose_name='نویسنده')
    Description = models.TextField(verbose_name="شرح")
    Slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس مخصوص مقاله")
    Thumbnail = models.ImageField(upload_to="images", verbose_name="تصویر مقاله")
    Published = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    Created = models.DateTimeField(auto_now_add=True, verbose_name="ساخته شده در")
    Updated = models.DateTimeField(auto_now=True, verbose_name="آخرین بروز رسانی در")
    Status = models.CharField(max_length= 1, choices=STATUS_CHOICES, verbose_name="وضعیت انتشار")
    
    objects = ArticleManager() # change the default manager to custom one
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ['-Published']
        
        
    def __str__(self):
        return self.Title
    
    
    def publish_time(self):
        return persian_calender_datetime(self.Published)
    publish_time.short_description = "زمان انتشار"

    
    def thumbnail_tag(self):
        return format_html("<img src={} width= 100  height = 80  style = 'border-radius: 5px;'  >".format(self.Thumbnail.url))
    thumbnail_tag.short_description = "عکس"


    def Category_str(self):
        return "، ".join([Category.Title for Category in self.Category.published()])
    Category_str.short_description = "دسته بندی ها"


    def get_absolute_url(self):
        return reverse("account:home")
    