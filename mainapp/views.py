#all the imports needed
#python 
import re #expressions régulières

#django
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
#app
from .models import Clue, UserClues
from .forms import NewClueForm, QuestionForm


#simple function which return the index page
@login_required
def historic_view(request):
    return render(request, 'mainapp/historic.html', locals())

@login_required
def map_view(request):
    return render(request, 'mainapp/map.html', locals())

#login required?
"""def clues_view(request):
    if request.method == 'POST':
        form = cluesForm(request.POST)
        if form.is_valid():
            # recup des infos
            name = form.cleaned_data["name"]
            content = form.cleaned_data["content"]
            email = form.cleaned_data["email"]
            
            #creation d'une nouvelle ligne pour le model de clues
            new_mail = clues(name=name, email=email, content=content)
            new_mail.save()
            messages.success(request, 'Votre message a bien été envoyé')
            return redirect('clues')

            #here goes the success message and the redirecting
            
    else:
        form = cluesForm()
    return render(request, 'mainapp/clues.html', locals())"""

@login_required
def list_clues_view(request):
    #Formulaire pour un nouvel indice
    if request.method == "POST":
        form = NewClueForm(request.POST)
        #si le formulaire est valide, on enregistre l'indice correspondant sur le user connecté
        if form.is_valid():
            newClue = UserClues()
            newClue.player = request.user
            #Message d'erreur si le nombre rentré n'est pas dans les chiffre de la base

            #-------------------Gestion erreurs----------------------

            present = False
            for y in Clue.objects.filter(code = form.cleaned_data["code"]):
                if y.code == form.cleaned_data["code"]:
                    present = True

            if present: #si le nombre existe bien dans la base
                newClue.clue = Clue.objects.get(code = form.cleaned_data["code"])

            else:               
                messages.error(request, 'Cette indice n\'est pas valide')
                return redirect('list_clues')
                #redirect



            ##Vérif des doublons pour ne pas surcharger la base et ne pas mettre deux fois le meme indice##
            doublon = False

            for x in UserClues.objects.filter(player = request.user):
                if newClue.clue == x.clue:
                    doublon = True

            if doublon:
                messages.error(request, 'vous avez déjà tapé cet indice. Vous pouvez le revoir dans la liste ci-dessous.') #message d'erreur Puis rediredt list
            else:
                newClue.save()

                if newClue.clue.optional_question:
                    return redirect('question', id_clue=newClue.id)

                else:
                    newClue.save()

                    #redirection vers l'indice tapé si il n'y a pas de doublon
                    return redirect('content_clue', id_clue=newClue.id)
                #-----------------------------------------------------------------

            form = NewClueForm()#remise à blanc
            ###################################

            

    else:
        form = NewClueForm()

    #Affichage de la liste des indices
    clues = UserClues.objects.filter(player = request.user)
    #mettre un order by avec la date de parution de l'indice


    return render(request, 'mainapp/list_clues.html', {'clues':clues, 'form': form})

@login_required
def content_clue(request, id_clue):
    #messages.warning(request, 'Votre dernière destination : {}'.format(UserClues.objects.get(id=id_clue).clue.title)) #On prepare un message afficher lors de l'actualisation de la page (quand il sera revenu sur la liste)
    #On sélectionne l'indice dont l'id à été choisi
    try:
        whole_clue = UserClues.objects.get(id=id_clue)
    except whole_clue.DoesNotExist:
        raise Http404
    #On fait du nombre une chaine de caracter pour la mettre dans l'url de l'image
    code = str(whole_clue.clue.code)
    #-------------------------------------------------
    #On retourne l'indice complet
    return render(request,'mainapp/content_clue.html',{'whole_clue':whole_clue,'code':code}, )



def question_view(request, id_clue):

    try:
        whole_clue = UserClues.objects.get(id=id_clue)
    except whole_clue.DoesNotExist:
        raise Http404
    #On fait du nombre une chaine de caracter pour la mettre dans l'url de l'image
    code = str(whole_clue.clue.code)
    #-------------------------------------------------

    ##optional_question = whole_clue.clue.optional_question
    #optional_answer = whole_clue.clue.optional_answer
    #On supprime la question optionnelle de l'indice de l'user et que de lui
    #Formulaire pour un nouvel indice
    if request.method == "POST":
        form = QuestionForm(request.POST)
        #si le formulaire est valide,
        if form.is_valid():
            #si la réponse est correcte
            if whole_clue.clue.optional_answer == form.cleaned_data["answer"]:
                return redirect('content_clue', id_clue=id_clue)
                #-----------------------------------------------------------------
            else:
                messages.error(request, 'Vous avez dû manquer une étape avant ce lieu')
                whole_clue.delete()
                return redirect('list_clues')

            form = QuestionForm()#remise à blanc
            ###################################

            

    else:
        form = QuestionForm()

    #Affichage de la liste des indices


    return render(request,'mainapp/question.html',{'form': form, 'whole_clue':whole_clue}, )



#on supprime l'indice non trouvé et on décale vers la liste
def list_clues_question_view(request, id_clue):
    try:
        whole_clue = UserClues.objects.get(id=id_clue)
    except whole_clue.DoesNotExist:
        raise Http404

    whole_clue.delete()
    return redirect('list_clues')