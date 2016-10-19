
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Question
from django.template import loader

def hello_poll(request):
    return HttpResponse("Polls View!")

def second_poll(request):
    return HttpResponse("second Polls View!")

def index(request):
   #p=new Question
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))