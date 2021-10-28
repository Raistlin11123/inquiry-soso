from . import views
from django.urls import path

urlpatterns = [
    #Maybe a generic view?
    path('historic', views.historic_view, name='historic'),
    path('map', views.map_view, name='map'),
    path('list_clues', views.list_clues_view, name='list_clues'),
    path('content_clue/<int:id_clue>', views.content_clue, name='content_clue'),
    path('question/<int:id_clue>', views.question_view, name='question'),
    path('list_clues_question/<int:id_clue>', views.list_clues_question_view, name='list_clues_question')
]