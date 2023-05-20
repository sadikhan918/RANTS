from django import forms
from django.contrib.auth.models import User
import datetime

class registerUser(forms.Form):
    username = forms.CharField(label="Enter Username", max_length=50)
    password = forms.CharField(label="Enter Password")
    email = forms.CharField(label="Enter Email")

class makeRant(forms.Form):
    username = User.username
    rantText = forms.CharField(widget=forms.Textarea, label="Enter RANT")
    rantDate = datetime.date.today()