from django.shortcuts import render


def article_home(request):
    return render(request, 'article/base.html')
