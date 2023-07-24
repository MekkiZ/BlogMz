from django.shortcuts import render, redirect
from .models import UserCus
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login


def signup(request):

    if request.method == 'POST' and 'images' in request.FILES:
        username=request.POST['username']
        email = request.POST['email']
        password=request.POST['password']
        succes_message = 'Votre compte a etais cree avec succes'

        error_message = "Attention votre mots de passe n'est pas correct"
        error_message_user = 'Cette utilisateur existe deja'

        if UserCus.objects.filter(Q(username=username)and
                                  Q(password=password)and
                                  Q(mail=email)):
            return render(request, 'authenticate/signup.html', context={'error_user':error_message_user})
        else:
            if len(password) > 8 and password == request.POST['password2']:

                for letter in password:
                    if password[0].isupper() and letter.isdigit():
                        print('je usis asser ici ')
                        new_user = UserCus(username=username.lower(),
                                           mail=email,
                                           password=password,
                                           job=request.POST['job'],
                                           image=request.FILES['images'])
                        new_user.set_password(password)
                        new_user.save()
                        succes_message = messages.success(request, succes_message)
                        redirect('login')
            else:
                error_message = messages.error(request, error_message)
            return render(request, 'authenticate/signup.html', context={'error':error_message, 'succes':succes_message})

    return render(request, 'authenticate/signup.html')


def login_user(request):
    if request.method == 'POST':
        email=request.POST['email']
        username=UserCus.objects.get(mail=email).username
        print(username)
        password=request.POST['password']
        user = authenticate(request, username='mekki', password='Mekki75020.')
        print(user)
        if user is not None:
            login(request, user)
            print('je suis ici')
            return redirect('home')
        else:
            messages.error(request, 'Error pendant la connexion veuillez reesayer')
    else:
        messages.error(request,"un probleme est survenu pendant l'envoi des donnees")

    return render(request, 'authenticate/login.html')