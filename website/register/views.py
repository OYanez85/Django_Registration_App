from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# from django.views.generic.edit import FormView
# from signup.forms import SignupForm
# Create your views here.

def index(request):
    return HttpResponse("View: registration index")

from .forms import RegForm

def reg_view(request):
    context = {}
    context['form']=RegForm()
    return render(request, "reg.html", context)

# class SignupFormView(FormView):
    # this must be the template
    # template_name = "reg.html"
    # form_class = SignupForm
    # for now, just return to the same page
    # success_url = ''

# Add this function to the file
def signup_view(request):
    return HttpResponse("Welcome to the signup page!")

from django.views.generic.edit import FormView

class RegFormView(FormView):
    template_name = "reg.html"
    form_class = RegForm
    success_url = 'reg_complete'
    
    def form_valid(self, form):
        print(form.data)
        return super().form_valid(form)

def reg_complete(request):
    return HttpResponse("Registration complete!")