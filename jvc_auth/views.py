from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import generic

from .forms import LoginForm

# Create your views here.

class UserLoginView(generic.View):
    form_class = LoginForm
    template_name = 'login.html'
    
    # SPECIFY GET METHOD (for ALL generic views?)
    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'login_form': form})
    
    # SPECIFY POST METHOD
    def post(self, request):
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username = username, password = password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'You are logged in as { username }')
                return redirect('home')
            else:
                messages.error(request, 'Error')
        else:
            messages.error(request, "Username or Password incorrect")
        return render(request, 'login.html', { 'login_form': form })
    
class UserLogout(generic.View):
    
    def get(self, request):
        logout(request)
        return redirect('home')

# def login_user(request):
    # return render(request, 'login.html', {})