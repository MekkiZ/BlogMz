
from django.contrib import admin
from django.urls import path
from article import views as v_article
from authenticate import views as v_auth
from posts import views as v_posts
from profil import  views as v_profil

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v_article.article_home, name='home'),
    # Article Part
    path('create_article_adm/', v_article.create_article, name='article_for_admin'),
    path('update_ur_article/<int:id>',v_article.update_article_by_id, name='update_article'),
    path('delete_article/<int:id>', v_article.delete_article_by_id, name='delete_article'),
    path('articles/', v_article.articles, name='articles'),
    path('article_only_one/', v_article.articles, name='article_one'),
    # Authenticate Part
    path('login/', v_auth.login_user, name='login'),
    path('signup/', v_auth.signup, name='signup'),
    # Posts and followings Part
    path('posts/', v_posts.my_posts, name='posts'),
    path('followings/', v_posts.following, name='followings'),
    # Profil and Dashboard part
    path('salon/', v_profil.dash),

]
