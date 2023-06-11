from django.shortcuts import render, get_object_or_404,redirect
from projects.forms import StudentSignUpForm, LoginForm, TeacherSignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import  (View,TemplateView,
                                  ListView,DetailView,
                                  CreateView,UpdateView,
                                  DeleteView)
from projects import models
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def SignUp(request):
    return render(request,'classroom/signup.html',{})

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def news_view(request):
    return render(request, 'news.html')

def student_register_view(request):
    msg = None
    if request.method == "POST":
        form = StudentSignUpForm(request.POST)

        if form.is_valid():

            userobj = form.save()
            userobj.is_student = True
            userobj.save()
            msg = 'user created'

            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = StudentSignUpForm()
    return render(request,'student_register.html', {'form':form, 'msg': msg})

def teacher_register_view(request):
    msg = None
    if request.method == "POST":
        form = TeacherSignUpForm(request.POST)

        if form.is_valid():

            userobj = form.save()
            userobj.is_teacher = True
            userobj.save()
            msg = 'user created'

            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = TeacherSignUpForm()
    return render(request,'teacher_register.html', {'form': form, 'msg': msg})

#class SignUpView(generic.CreateView):
   # form_class = SignUpForm
    #template_name = AUTHENTICATION_APP/register.html
    #success_url = reverse_lazy('some:reversed_url')

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_student:
                login(request, user)
                return redirect('student_profile_view')
            elif user is not None and user.is_teacher:
                login(request, user)
                return redirect('teacher_profile_view')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def student_profile_view(request):
    return render(request,'student_profile.html')


def teacher_profile_view(request):
    return render(request,'teacher_profile.html')

## logout view.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def signup_view(request):
    return render(request,'signup.html',{})
