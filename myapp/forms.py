
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Post, Profile
import datetime


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))
    date_joined =datetime.datetime.now()

    class Meta:
        model = User
        fields= ['username','email','first_name','last_name','password1','password2']
        widgets = {'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),
                   'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}),
                   'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}),
                   'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}),}
                   

class FormPasswordChange(PasswordChangeForm):
    
    old_password = forms.CharField(label='Old Password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='Confirm New Password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))            



class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields= ['username','email','first_name','last_name']
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
                   'first_name':forms.TextInput(attrs={'class':'form-control'}),
                   'last_name':forms.TextInput(attrs={'class':'form-control'}),
                   'email':forms.EmailInput(attrs={'class':'form-control'}),}
                   


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields =['image','status','qualification','profession','about']
        widgets ={
             'qualification':forms.TextInput(attrs={'class':'form-control'}),
             'profession':forms.TextInput(attrs={'class':'form-control'}),
             'about':forms.Textarea(attrs={'class':'form-control','rows':2,'cols':3,}),
             'status':forms.Select(attrs={'class':'form-control'}),
             }


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields= ['title','description']
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
                   'description':forms.Textarea(attrs={'rows':2,'cols':3,'class':'form-control'}),}
