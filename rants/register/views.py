from django.shortcuts import render, redirect
from .forms import registerUser

# Create your views here.
def register(response):
    if response.method == 'POST':
        form = registerUser(response.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = registerUser()
    return render(response, 'register/register.html', {'form':form})