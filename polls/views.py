
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Question
from django.template import loader
from django.utils import timezone

def hello_poll(request):
    return HttpResponse("Polls View!")

def second_poll(request):
    return HttpResponse("second Polls View!")

def question_detail(request,question_id):
    return HttpResponse("The question which you are asking is %s."%question_id)

def index(request):
   #p=new Question
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def create_question(request):
    return render(request,'polls/create_question.html')

def create_now(request):
    q=Question(question_text="What's next now thrid?", pub_date=timezone.now())
    q.save()
    return HttpResponse("successfully")
