from django.shortcuts import render


def article_home(request):
    return render(request, 'article/articles.html', {'range': range(3)})


def one_article_by_id(request):
    return render(request, 'article/one_article_page.html')
