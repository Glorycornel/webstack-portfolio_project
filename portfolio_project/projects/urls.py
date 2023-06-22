from django.urls import path
from . import views

#from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name= 'home'),
    path('login/', views.login_view, name='login_view'),
    path('teacher_register/', views.teacher_register_view, name='teacher_register_view'),
    path('student_register/', views.student_register_view, name='student_register_view'),
    path('<int:user_id>/student_profile/', views.student_profile_view, name='student_profile_view'),
    path('studentupdate_profile/', views.studentupdate_profile_view, name='studentupdate_profile_view'),
    path('studentscore_board/', views.studentscore_board_view, name='studentscore_board_view'),
    path('teacher_scoreboard/', views.teacher_scoreboard_view, name='teacher_scoreboard_view'),
    path('uploadtask/', views.uploadtask_view, name='uploadtask_view'),
    path('submittask/', views.submittask_view, name='submittask_view'),
    path('<int:user_id>/teacher_profile/', views.teacher_profile_view, name='teacher_profile_view'),
    path('teacherupdate_profile/', views.teacherupdate_profile_view, name='teacherupdate_profile_view'),
    path('about/', views.about_view, name='about_view'),
    path('contact/', views.contact_view, name='contact_view'),
    path('news/', views.news_view, name='news_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('logout/', views.logout_view, name='logout'),
]