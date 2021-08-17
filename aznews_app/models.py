from django.db import models
from django.templatetags.static import static
from django.urls import reverse

'''
Page
=======
About us
Contact


News
======
title
content
category
image
created_at
updated_at
views

Categories
==========
slug
title (
Lifestyle
Travel
Fashion
Sports
Technology
Concert
Sea Beach
Bike show
Skeping
)
'''


class Page(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    preview = models.ImageField(upload_to='previews/%Y/%m/%d', blank=True)

    def image_tag(self):
        from django.utils.html import escape
        return u'<img src="%s" />' % escape

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __str__(self):
        return self.title


class News(models.Model):
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = verbose_name

    title = models.CharField(max_length=60)
    content = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    preview = models.ImageField(upload_to='previews/%Y/%m/%d', blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    views = models.IntegerField(default=0)
    slug = models.SlugField(max_length=60)

    def preview_or_default(self, default_path=static('img/gallery/4.jpg')):
        if self.preview:
            return self.preview.url
        return default_path

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news', kwargs={'slug': self.slug})


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    title = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60)

    def __str__(self):
        return self.title
