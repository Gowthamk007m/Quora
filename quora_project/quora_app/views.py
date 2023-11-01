import random
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from .forms import QuestionForm, AnswerForm
from . models import *
from django.urls import reverse
from django.db.models import Count
from random import sample

def frontpage(request):
    questions= Question.objects.annotate(answer_count=Count('answers')).order_by("-created_at")

    random_questions = list(Question.objects.all())

    num_random_questions = min(3, len(random_questions))

    random_questions = sample(random_questions, num_random_questions)
    return render(request, 'frontpage.html',{"Questions":questions,'random_questions':random_questions})

def All_Answers(request,pk):
    int_id=int(pk)
    answers=Answer.objects.filter(question_id=pk).order_by("-created_at")
    question=Question.objects.get(id=pk)

    return render(request,'answers.html',{"answers":answers,'qstn':question})

    


@login_required
def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user 
            question.save()

            
            return redirect('home_page')
        else:
            return redirect('home_page')
    else:
        form = QuestionForm()
        
    
    return render(request, 'frontpage.html', {'form': form})

@login_required
def create_answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    string_id=str(question_id)
    
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user 
            answer.question = question  
            answer.save()
            return redirect(reverse('view_answers',args=(string_id,)))
    else:
        form = AnswerForm()
    
    return render(request, 'frontpage.html', {'form': form, 'question': question})

@login_required
def delete_question(request,id):
    qstn = get_object_or_404(Question, id=id)
    qstn.delete()
    return redirect('home_page')


@login_required
def delete_answer(request,id,pk):
    string_id=str(pk)
    ans = get_object_or_404(Answer, id=id)
    ans.delete()
    return redirect(reverse('view_answers', args=(string_id,)))


@login_required
def like_answers(request,pk,q_id):
    string_id=str(q_id)

    get_answer=get_object_or_404(Answer,id=pk)

    if get_answer.likes.filter(id=request.user.id):
        get_answer.likes.remove(request.user)

    else:
        get_answer.likes.add(request.user)

    return redirect(reverse('view_answers', args=(string_id,)))

