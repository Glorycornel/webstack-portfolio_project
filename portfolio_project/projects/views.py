from django.shortcuts import render, get_object_or_404,redirect
from projects.forms import StudentProfileForm, LoginForm, TeacherProfileForm, UserForm
from django.contrib.auth.decorators import login_required
from projects import models
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.urls import reverse
from . models import Student, Teacher

# Create your views here.
def home(request):
    return render(request, 'home.html')

def SignUp(request):
    return render(request,'signup.html',{})

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def news_view(request):
    return render(request, 'news.html')


def student_register_view(request):
    user_type = 'student'
    registered = False

    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        student_profile_form = StudentProfileForm(data = request.POST)

        if user_form.is_valid() and student_profile_form.is_valid():

            user = user_form.save()
            user.is_student = True
            user.save()

            profile = student_profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
            return redirect('login_view')
        else:
            print(user_form.errors,student_profile_form.errors)
    else:
        user_form = UserForm()
        student_profile_form = StudentProfileForm()

    return render(request,'student_register.html',{'user_form':user_form,'student_profile_form':student_profile_form,'registered':registered,'user_type':user_type})


# def student_register_view(request):
#     msg = None
#     if request.method == "POST":
#         form = StudentSignUpForm(request.POST)

#         if form.is_valid():

#             userobj = form.save()
#             userobj.is_student = True
#             userobj.save()
#             msg = 'user created'

#             return redirect('login_view')
#         else:
#             msg = 'form is not valid'
#     else:
#         form = StudentSignUpForm()
#     return render(request,'student_register.html', {'form':form, 'msg': msg})



def teacher_register_view(request):
    user_type = 'teacher'
    registered = False

    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        teacher_profile_form = TeacherProfileForm(data = request.POST)

        if user_form.is_valid() and teacher_profile_form.is_valid():

            user = user_form.save()
            user.is_teacher = True
            user.save()

            profile = teacher_profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
            return redirect('login_view')
        else:
            print(user_form.errors,teacher_profile_form.errors)
    else:
        user_form = UserForm()
        teacher_profile_form = TeacherProfileForm()

    return render(request,'teacher_register.html',{'user_form':user_form,'teacher_profile_form':teacher_profile_form,'registered':registered,'user_type':user_type})

# def teacher_register_view(request):
#     msg = None
#     if request.method == "POST":
#         form = TeacherSignUpForm(request.POST)

#         if form.is_valid():

#             userobj = form.save()
#             userobj.is_teacher = True
#             userobj.save()
#             msg = 'user created'

#             return redirect('login_view')
#         else:
#             msg = 'form is not valid'
#     else:
#         form = TeacherSignUpForm()
#     return render(request,'teacher_register.html', {'form': form, 'msg': msg})

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
                return HttpResponseRedirect(reverse('student_profile_view', args=(user.id,)))
            elif user is not None and user.is_teacher:
                login(request, user)
                return HttpResponseRedirect(reverse('teacher_profile_view', args=(user.id,)))
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})

def student_profile_view(request, user_id):
    student = Student.objects.get(pk = user_id)
    return render(request,'student_profile.html',{"student": student})


def teacher_profile_view(request, user_id):
    teacher = Teacher.objects.get(pk = user_id)
    return render(request,'teacher_profile.html',{"teacher": teacher})


def studentupdate_profile_view(request):
    return render(request,'studentupdate_profile.html',{})

def teacherupdate_profile_view(request):
    return render(request,'teacherupdate_profile.html',{})


def studentscore_board_view(request):
    return render(request,'studentsscore_board.html',{})


def teacher_scoreboard_view(request):
    return render(request,'teacher_scoreboard.html',{})


def uploadtask_view(request):
    return render(request,'uploadtask.html',{})

def submittask_view(request):
    return render(request,'submittask.html',{})



## logout view.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def signup_view(request):
    return render(request,'signup.html',{})
