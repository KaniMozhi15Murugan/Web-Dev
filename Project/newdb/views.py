# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User

# # Create your views here.

# def register(request):

#     if request.method == "POST":
#         first_name = request.POST["first_name"]
#         last_name = request.POST["last_name"]
#         username = request.POST["username"]
#         email = request.POST["email"]
#         password = request.POST["password"]
#         passwords = request.POST["passwords"]



 
#         user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password,passwords=passwords)
#         user.save();
    
#         return redirect("/")
    
#     else:  
#         return render(request, 'register.html')



from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        passwords = request.POST["passwords"]

        # Check if passwords match
        if password != passwords:
            messages.error(request, "Passwords do not match.")
            return render(request, 'register.html')

        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.save()
        
        messages.success(request, "Registration successful. You can now login.")
        return redirect("/")
    
    else:  
        return render(request, 'register.html')
