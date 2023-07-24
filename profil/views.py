from django.shortcuts import render

def dash(request):
    return render(request, 'profil/Salon.html')



def signup(request):
    return render(request, 'authenticate/signup.html')

