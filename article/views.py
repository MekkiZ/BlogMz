from django.shortcuts import render


def article_home(request):
    return render(request, 'article/index_website.html', {'range': range(3)})


def articles(request):
    return render(request, 'article/articles.html')


def one_article_by_id(request):
    return render(request, 'article/one_article_page.html')


def create_article(request):
    return render(request, 'article/create_article.html')


def delete_article_by_id(request):
    return render(request, 'article/delete_article.html')


def update_article_by_id(request):
    return render(request, 'article/update_article.html')
