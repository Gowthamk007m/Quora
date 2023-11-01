from django.urls import path
from .views import *

urlpatterns = [
    path('',frontpage, name='home_page'),
    path('create_question/',create_question, name='create_question'),

    path('answers/<str:pk>/',All_Answers, name='view_answers'),

    path('like/<int:pk>/<int:q_id>/',like_answers, name='like_answers'),


    path('create_answer/<int:question_id>/',create_answer, name='create_answer'),


    path('delete_answer/<int:id>/<int:pk>/',delete_answer, name='delete_answer'),
    


    path('delete/<int:id>/',delete_question, name='delete_question'),


]
