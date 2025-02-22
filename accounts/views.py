from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView


def register_view(request):
    if request.method=='POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    else:
        user_form = UserCreationForm()
    return render(request,'accounts/register.html',{'user_form': user_form})

class AccountLoginView(LoginView):
    next_page = 'home'
    
