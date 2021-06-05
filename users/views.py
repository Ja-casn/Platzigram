"""Users views."""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def login_view(request):
    """Login view."""
    if request.method == 'POST':
        print('*' * 10)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # Redirect to a success page.
            return redirect('feed')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})
    return render(request, 'users/login.html')

def signup(request):
    """Sign up view."""
    return render(request, 'users/signup.html')
    
@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('login')