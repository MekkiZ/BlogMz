
from django.contrib import admin
from django.urls import path
from article import views as v_article

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v_article.article_home)
]
