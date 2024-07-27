from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if user.user_type == 'admin':
                return redirect('admin_home')
            elif user.user_type == 'doctor':
                return redirect('doctor_home')
            elif user.user_type == 'patient':
                return redirect('patient_home')
    return render(request, 'login.html')

@login_required
def admin_home(request):
    return render(request, 'admin_home.html')

@login_required
def doctor_home(request):
    return render(request, 'doctor_home.html')

@login_required
def patient_home(request):
    return render(request, 'patient_home.html')
