from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Question, Choice
from django import views
from django.contrib.auth.mixins import LoginRequiredMixin as LoginR
from .forms import pollForm
    
class index(LoginR, views.View):
    def index(self, request):
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        context = {'latest_question_list': latest_question_list}
        return render(request, 'polls/index.html', context)
class detail(LoginR, views.View):
    def detail(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/detail.html', {'question': question})
class results(LoginR, views.View):
    def results(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/results.html', {'question': question})
class vote(LoginR, views.View):
    def vote(self, request, question_id):
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



    #Coursera Stuff

def owner(request):
    page = render(request, "polls/owner.html")
    return page

def main(request):
    ret = render(request, "home/main.html")
    return ret

    # Cookies
    from django.http import cookie

class cookie_jar(LoginR, views.View):
    #Adds a cookie called "cookie" with the valie of "Jack's cookie"
    def cookie_jar(self, request):
        print(request.COOKIES)
        print("User requests cookies!")
        resp = HttpResponse("Cookie")
        resp.set_cookie("cookie", "Jack's cookie")
        return resp

class rmcookie(LoginR, views.View):
    #Removes the cookie "cookie"
    def remove_cookie(self, request):
        resp = HttpResponse("Cookie Removed")
        resp.delete_cookie("cookie", "/", "127.0.0.1")
        return resp
