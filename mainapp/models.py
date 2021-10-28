from django.db import models
from django.contrib.auth.models import User
import datetime

now = datetime.datetime.now()

"""
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    
    def __str__(self):
        return "Message de {}".format(self.name)
"""

class Clue(models.Model):
	title = models.CharField(max_length=42, verbose_name='Titre')
	url_img_optionnel =  models.CharField(max_length=42, default= 'rien', verbose_name='url_img_optionnel')#rien si il n'y a pas d'image

	paragraph1 = models.TextField(verbose_name = 'paragraph1', null=True, blank=True)

	code = models.CharField(null=True, verbose_name="code", max_length=30) #code pour accéder à l'indice
	#question d'entrée optionnel (réponse)
	optional_question = models.CharField(null=True, verbose_name="question optionelle", max_length=255, blank=True)
	optional_answer = models.CharField(null=True, verbose_name="réponse optionelle", max_length=255, blank=True)


	def __str__(self):
		return "{}".format(self.title)

class UserClues(models.Model):
	player = models.ForeignKey(User, on_delete=models.CASCADE)
	clue = models.ForeignKey(Clue, on_delete=models.CASCADE)
	date = models.DateTimeField(default=now, blank=True)


	def __str__(self):
		return "indice de {}".format(self.player.username)
#trouver un nom singulier autre que UserClue (déjà utilisé par django)