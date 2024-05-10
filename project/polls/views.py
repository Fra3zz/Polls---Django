from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django import views
from django.contrib.auth.mixins import LoginRequiredMixin as LoginR
from .models import Question, Choice
from .forms import pollForm

class Index(LoginR, views.View):
    def get(self, request):
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        context = {'latest_question_list': latest_question_list}
        return render(request, 'polls/index.html', context)

class Detail(LoginR, views.View):
    def get(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/detail.html', {'question': question})

class Results(LoginR, views.View):
    def get(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/results.html', {'question': question})

class Vote(LoginR, views.View):
    def post(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class Owner(LoginR, views.View):
    def get(self, request):
        return render(request, "polls/owner.html")

class Main(LoginR, views.View):
    def get(self, request):
        return render(request, "home/main.html")

class CookieJar(LoginR, views.View):
    def get(self, request):
        print(request.COOKIES)
        print("User requests cookies!")
        resp = HttpResponse("Cookie")
        resp.set_cookie("cookie", "Jack's cookie")
        return resp

class RemoveCookie(LoginR, views.View):
    def get(self, request):
        resp = HttpResponse("Cookie Removed")
        resp.delete_cookie("cookie", "/", "127.0.0.1")
        return resp