from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.


class User(AbstractUser):
    is_student = models.BooleanField('Is student', default=False)
    is_teacher = models.BooleanField('Is teacher', default=False)

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='Student')
    first_name=models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    student_profile_pic = models.ImageField(upload_to="classroom/student_profile_pic",blank=True)

    def get_absolute_url(self):
        return reverse('student_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']

class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='Teacher')
    first_name=models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    subject_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    teacher_profile_pic = models.ImageField(upload_to="classroom/teacher_profile_pic",blank=True)

    def get_absolute_url(self):
        return reverse('teacher_detail',kwargs={'pk':self.pk})

    def __str__(self): 
        return self.first_name