from django.db import models
from django.utils import timezone
from extensions.persian_datetime import persian_calender_datetime

class Categories(models.Model):
    Title = models.CharField(max_length=200, verbose_name="عنوان دسته بندی")
    Slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس مخصوص دسته بندی")
    Position = models.IntegerField(verbose_name="جایگاه")
    Status = models.BooleanField(default=1, verbose_name="آیا منتشر شود؟")
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ["Position"]
    def __str__(self):
        return self.Title
    

class Article(models.Model):
    STATUS_CHOICES = (
        ('p','منتشر شده'),
        ('d','پیش نویس')
    )
    
    Title = models.CharField(max_length=200, verbose_name="عنوان")
    Category = models.ManyToManyField(Categories, verbose_name="دسته بندی")
    Description = models.TextField(verbose_name="شرح")
    Slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس مخصوص مقاله")
    Thumbnail = models.ImageField(upload_to="images", verbose_name="تصویر مقاله")
    Published = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    Created = models.DateTimeField(auto_now_add=True, verbose_name="ساخته شده در")
    Updated = models.DateTimeField(auto_now=True, verbose_name="آخرین بروز رسانی در")
    Status = models.CharField(max_length= 1, choices=STATUS_CHOICES, verbose_name="وضعیت انتشار")
    
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ['-Published']
        
        
    def __str__(self):
        return self.Title
    
    def publish_time(self):
        return persian_calender_datetime(self.Published)
    publish_time.short_description = "زمان انتشار"
    
    