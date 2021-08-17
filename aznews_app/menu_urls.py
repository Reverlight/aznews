from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from aznews_app.views.menu import home_page, whats_new_page, about_page,news_page

urlpatterns = [
    path('home', home_page, name='home'),
    path('whats_new', whats_new_page, name='whats_new'),
    path('about', about_page, name='about'),
    path('news', news_page, name='news'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
