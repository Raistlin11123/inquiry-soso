#all the imports needed
#django import
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
#apps import
from .forms import LoginForm, SignupForm


# Create your views here.
def login_view(request):
    error = False
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
                
            user = authenticate(username=username, password=password)  # We check wither the data are correct
            if user:  # If the object returned is not None
                messages.warning(request, "Bienvenue, mon ami. Il faut être vif avant que le meurtrier de ma femme ne s'échappe!")
                login(request, user)  # We log the user in
                return redirect('historic')
             
            else:
                messages.error(request, 'Identifiant ou mot de passe incorrect')
                return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', locals())


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid(): 
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            password_confirmation = form.cleaned_data.get('password_confirmation')
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            
            #Le mot de passe doit faire au moins 8 caractères pour être haché par django
            if len(password) < 6:
                messages.error(request, 'Le mot de passe doit avoir au minimum 6 caractères')
                return redirect('signup')

            #vérification pseudo non utilisé
            double_username = User.objects.filter(username=username)
            if double_username:
                messages.error(request, 'Ce pseudo existe déjà')
                return redirect('signup')



            #vérification des deux mots de passes
            if password == password_confirmation:
                
                user = User()

                user.username = username
                user.set_password(password)
                user.email = email
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                
                user = authenticate(username=username, password=password)
                
                login(request, user)
                messages.warning(request, "Bienvenue, mon ami. Il faut être vif avant que le meurtrier de ma femme ne s'échappe!")
                return redirect('historic')
            #si les 2 mdp sont différents
            else:
                messages.error(request, 'Le mot de passe de confirmation est différent du mot de passe')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def logout_view(request):
    	logout(request)
    	return redirect('login')
	#We redirect the user on the connexion page


