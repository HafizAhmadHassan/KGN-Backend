from django.shortcuts import render

# Create your views here.

from polls.models import Question
from django.template import loader

from django.shortcuts import render
from django.db.models import F
from django.http import HttpResponse,Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question

from django.core.mail import send_mail

import smtplib



def index(request):

    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    try:
        content="Hello World"
        """
        content="Hello World"
        from django.core.mail import send_mail

        import smtplib
        mail=smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        sender='ahmadhassan061@gmail.com'
        recipient='develop@kgn.it'
        mail.login('ahmadhassan061@gmail.com','jtjrwpaxovfqsgxv')
        header='To:'+ recipient +'\n'+'From:' \
        +sender+'\n'+'subject:testmail\n'
        content=header+content
        mail.sendmail(sender, recipient, content)
        mail.close()

        """

        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"]) # return id of selected chouce
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        #F("votes") + 1 instructs the database to increase the vote count by 1.
        selected_choice.votes= F("votes") + 1
        selected_choice.save()
# you should always return an HttpResponseRedirect after successfully dealing with POST data.
        print("Hi ",question.id)
        print(question) 
        #reverse function helps avoid having to hardcode a URL in the view function.

        # question.id used because of this for example

        # "/polls/3/results/" there is 3
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))