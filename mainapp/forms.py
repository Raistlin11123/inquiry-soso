from django import forms

"""class ContactForm(forms.Form):
    name = forms.CharField(label="", max_length=30, widget= forms.TextInput(attrs={'placeholder':'Nom', 'class': "form-control"}))
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'placeholder':'Email', 'class': "form-control"}))
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder':'Ecrivez votre message ici ...', 'class': "form-control", }))
"""
#Formulaire qui ajoute un indice a un joueur
class NewClueForm(forms.Form):
	code = forms.CharField(label="", max_length=30, widget= forms.TextInput(attrs={'placeholder':'Entrez le code', 'class': "form-control"}))

#formulaire pour la question optionnelle pour vérifie le passage
class QuestionForm(forms.Form):
	answer = forms.CharField(label="", max_length=255, widget= forms.TextInput(attrs={'placeholder':'Entrez la réponse', 'class': "form-control"}))