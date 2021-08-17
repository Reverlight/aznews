from django.core.paginator import Paginator
from django.db.models import Max
from django.shortcuts import render, redirect
from aznews_app.models import Category, News


def news_page(request):
    news = News.objects.order_by('-created_at')
    paginator = Paginator(news, 2)
    num_pages = paginator.num_pages
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'news': news, 'page_obj': page_obj, 'num_pages': num_pages}
    return render(request, 'aznews_app/menu_pages/news.html', context)



def get_recent_news_by_categories():
    categories = Category.objects \
        .annotate(num_books=Max('news__views')) \
        .order_by('-num_books')

    recent_news_by_categories = []

    for category in categories:
        recent_news = category.news_set.all().order_by('-created_at')
        if recent_news:
            # Whole news query set have one category
            category = recent_news[0].category
            recent_news_by_category = {"category": category, 'recent_news': recent_news}
            recent_news_by_categories.append(recent_news_by_category)

    return recent_news_by_categories


def get_recent_news_general():
    recent_news_all_categories = News.objects \
                                     .order_by('-category__title', '-views') \
                                     .distinct('category__title')[0:5]

    return recent_news_all_categories


def whats_new_page(request):
    recent_news_general = get_recent_news_general()
    recent_news_by_categories = get_recent_news_by_categories()

    context = {
        'recent_news_all_categories': recent_news_general,
        'popular_category_and_its_recent_news': recent_news_by_categories
    }

    return render(request, 'aznews_app/menu_pages/whats_new.html', context)


def home_page(request):
    return redirect('main')
