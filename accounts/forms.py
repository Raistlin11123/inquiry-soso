from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="", max_length=30, widget= forms.TextInput(attrs={'placeholder':'Entrez votre pseudo', 'class': "form-control"}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'Entrez votre mot de passe', 'class': "form-control"}))

class SignupForm(forms.Form):
    #first_name = forms.CharField(label="", max_length=30, widget= forms.TextInput(attrs={'placeholder':'Prénom', 'class': "form-control"}))
    #last_name = forms.CharField(label="", max_length=30, widget= forms.TextInput(attrs={'placeholder':'Nom de famille', 'class': "form-control"}))
    #email = forms.EmailField(label="", max_length=50, widget= forms.EmailInput(attrs={'placeholder':'Adresse email', 'class': "form-control"}))
    username = forms.CharField(label="", max_length=30, widget= forms.TextInput(attrs={'placeholder':'Pseudo', 'class': "form-control"}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'Mot de passe', 'class': "form-control"}))
    password_confirmation = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'Confirmation du mot de passe', 'class': "form-control"}))