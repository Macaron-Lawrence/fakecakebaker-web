from django.db import models
from django.conf import settings

def user_directory_path(instance, filename):
    return instance.article.name + '/' + filename

class Article(models.Model):
    name = models.CharField("编号", max_length=12)
    title = models.CharField('左侧标题',max_length=20, default="时代系列|新装限时上架")
    time = models.CharField('日期', max_length=10, default="2021|11|11")
    classify = models.BooleanField('归类', default=True)
    form = models.CharField("形式", max_length=10, default='text')
    content = models.TextField('内容')
    is_active = models.BooleanField('是否活跃', default=True)

    def __str__(self):
        return self.title + ' / ' + self.name


class File(models.Model):
    article = models.ForeignKey(Article, verbose_name="编号", on_delete=models.CASCADE)
    file = models.ImageField("图片", upload_to= user_directory_path)
    def image_tag(self):
        from django.utils.safestring import mark_safe
        return mark_safe('<img src="%s" height=150 />' %('/static/images/article/' + str(self.file)))
    def image_name(self):
        return str(self.file)
    image_name.short_description = '图片名称'
    image_name.allow_tags = True
    image_tag.short_description = '预览'
    image_tag.allow_tags = True


# Create your models here.
