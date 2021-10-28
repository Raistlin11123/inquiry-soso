from django.contrib import admin
"""from .models import Contact

# Register your models here.
admin.site.register(Contact)"""
from .models import Clue, UserClues
# Register your models here.

class ClueAdmin(admin.ModelAdmin):
    list_display   = ('title', 'code',)
    ordering       = ('title', 'code')

class UserCluesAdmin(admin.ModelAdmin):
    list_display   = ('player', 'clue',)
    list_filter    = ('player', 'clue')
    ordering       = ('player', 'clue')
    search_fields  = ('player', 'clue')


admin.site.register(Clue, ClueAdmin)
admin.site.register(UserClues, UserCluesAdmin)

#Ajouter des tris