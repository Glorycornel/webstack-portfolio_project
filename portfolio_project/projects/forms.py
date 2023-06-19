from django import forms
from django.contrib.auth.forms import UserCreationForm
from projects.models import Student, User, Teacher
#from django.contrib.auth.forms import get_user_model

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username','password1','password2']
        widgets = {
                'username': forms.TextInput(attrs={'class':'answer'}),
                'password1': forms.PasswordInput(attrs={'class':'answer'}),
                'password2': forms.PasswordInput(attrs={'class':'answer'}),
                }
        
## Teacher Registration Form 
class TeacherProfileForm(forms.ModelForm):
    class Meta():
        model =  Teacher
        fields = ['first_name','last_name','phone','email']
        widgets = {
                'first_name' : forms.TextInput(attrs={'class':'answer'}),
                'last_name' : forms.TextInput(attrs={'class':'answer'}),
                'phone': forms.NumberInput(attrs={'class':'answer'}),
                'email': forms.EmailInput(attrs={'class':'answer'}),
                }
        

class StudentProfileForm(forms.ModelForm):
    class Meta():
        model =  Student
        fields = ['first_name','last_name','phone','email']
        widgets = {
                'first_name': forms.TextInput(attrs={'class':'answer'}),
                'last_name': forms.TextInput(attrs={'class':'answer'}),
                'phone': forms.NumberInput(attrs={'class':'answer'}),
                'email': forms.EmailInput(attrs={'class':'answer'}),
                }
        
