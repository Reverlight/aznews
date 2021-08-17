from django.shortcuts import render
from aznews_app.models import News


def single_news(request, slug):
    news_item = News.objects.get(slug=slug)
    news_item.views += 1
    news_item.save()
    context = {
        'news_item': news_item
    }
    return render(request, 'aznews_app/single_news.html', context)
