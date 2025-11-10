from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Feedback

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'placeholder': 'Email (optional)', 'class': 'input'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {'username': forms.TextInput(attrs={'placeholder': 'Username', 'class': 'input'})}

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name', 'class': 'input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your email (optional)', 'class': 'input'}),
            'message': forms.Textarea(attrs={'placeholder': 'Write your feedback...', 'rows': 4, 'class': 'textarea'}),
        }

class LoggedInFeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'placeholder': 'Write your feedback...', 'rows': 4, 'class': 'textarea'}),
        }