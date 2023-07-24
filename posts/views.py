from django.shortcuts import render

def my_posts(request):
    return render(request, 'posts/my_posts_flux.html')


def following(request):
    return render(request, 'posts/followers_following.html')

