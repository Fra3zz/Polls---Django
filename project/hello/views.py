from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django import views

# Create your views here.

def cookie(request):
    print(request.COOKIES)
    oldval = request.COOKIES.get('zap', None)
    resp = HttpResponse('In a view - the zap cookie value is '+str(oldval))
    if oldval : 
        resp.set_cookie('zap', str(int(oldval)+1)) # Convert to string before setting
    else : 
        resp.set_cookie('zap', '42')  # Set string value
    resp.set_cookie('sakaicar', '42', max_age=1000) # seconds until expire
    return resp

class cookieclass(LoginRequiredMixin, views.View):
    def get(self, request):  # Use 'self' parameter
        num_visits = self.request.session.get('num_visits', 0) + 1  # Access request using 'self'
        self.request.session['num_visits'] = num_visits 
        if num_visits > 4 : 
            del(self.request.session['num_visits'])
        resp = HttpResponse('view count='+str(num_visits))
        resp.set_cookie('dj4e_cookie', '37151652', max_age=1000) #Added for class and autograding identification
        return resp
