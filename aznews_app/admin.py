from django import forms
from django.utils.safestring import mark_safe

from aznews_app.models import Category, News, Page
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget


def image_generator(obj):
    return f'<a target="_blank" href="{obj.preview.url}"> <img src="{obj.preview.url}" width="100px"></a>'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


class PageAdmin(admin.ModelAdmin):
    fields = ('title', 'content', 'preview', 'get_preview')
    readonly_fields = ('get_preview',)

    def get_preview(self, obj):
        if obj.preview:
            preview_html = image_generator(obj)
            return mark_safe(preview_html)

    list_display = ('title', 'preview', 'get_preview')


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'preview', 'get_preview', 'created_at', 'updated_at', 'views')
    fields = ('title', 'content', 'category', 'preview', 'get_preview', 'views', 'slug')
    readonly_fields = ('get_preview',)
    prepopulated_fields = {'slug': ('title',)}
    form = NewsAdminForm

    def get_preview(self, obj):
        if obj.preview:
            preview_html = image_generator(obj)
            return mark_safe(preview_html)


class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)

admin.site.register(Page, PageAdmin)
# Register your models here.
