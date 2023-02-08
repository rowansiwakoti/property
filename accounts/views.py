from django.shortcuts import render, redirect
from django.contrib import messages, auth
from contacts.models import Contact
from .models import User
# from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST': # Form submission
        
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            if User.objects.filter(email=email).exists(): #The email on the left of the equal sign is the field in DB
                messages.error(request, 'This email already exists')
                return redirect('register')
            else:
                # Register successfully
                user= User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=email, phone=phone, password=password)

                # Login after registration
                # auth.login(request.user)
                # messages.success(request,'You are now logged in')
                # return redirect('index')

                user.save()
                messages.success(request,'You are now registered. Please log in.')
                return redirect('login')


        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')

def login(request):
    if request.method == 'POST': # Form submission
        # Login user
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')
            return redirect('login')

        user = auth.authenticate(request, email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'Email or password is invalid')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are now logged out')
        return redirect('index')

# @login_required(login_url='login')
def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts':user_contacts
    }
    return render(request,'accounts/dashboard.html',context)