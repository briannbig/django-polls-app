from urllib import response
from django.http import Http404
from django.shortcuts import HttpResponse, get_object_or_404, render
from django.template import loader

from polls.models import Question

# Create your views here.

def index(request):
    latest_questions_list = Question.objects.order_by('-pub_date')[:5]    
    context = {
        'latest_question_list': latest_questions_list
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)    
    return render(request, 'polls/details.html', {'question': question})

def results(request, question_id):
    response = "You're looking at results for question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)