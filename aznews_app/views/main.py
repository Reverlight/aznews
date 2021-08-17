from django.shortcuts import render
from aznews_app.models import News


def main_page(request):
    most_popular_news = News.objects.order_by('-views')
    recent_news = News.objects.order_by('-created_at')[0:4]
    context = {
        'most_popular_news': most_popular_news,
        'recent_news': recent_news
    }
    return render(request, 'aznews_app/home.html', context)
