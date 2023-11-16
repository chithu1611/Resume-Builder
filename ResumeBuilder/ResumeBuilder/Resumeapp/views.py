from django.shortcuts import render,redirect
from .form import CustomUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.




def home(request):
    return render(request,'Resumeapp/index.html')

def personal_details(request):
    return render(request,'Resumeapp/personal details.html')

def education(request):
    return render(request,'Resumeapp/education.html')

def Exp(request):
    return render(request,'Resumeapp/Exp.html')

def skills(request):
    return render(request,'Resumeapp/skills.html')

def obj(request):
    return render(request,'Resumeapp/obj.html')

    
def project(request):
    return render(request,'Resumeapp/project.html')


def eca(request):
    return render(request,'Resumeapp/ECA.html')

    
def aoi(request):
    return render(request,'Resumeapp/AOI.html')


def lang(request):
    return render(request,'Resumeapp/Lang.html')


def hobby(request):
    return render(request,'Resumeapp/Hobby.html')


def ach(request):
    return render(request,'Resumeapp/Achieve.html')

def temp(request):
    return render(request,'Resumeapp/template.html')

def res1(request):
    return render(request,'Resumeapp/Temp/Resume1.html')

def res2(request):
    return render(request, 'Resumeapp/Temp/Resume2.html')

def res3(request):
    return render(request,'Resumeapp/Temp/Resume3.html')

def res4(request):
    return render(request,'Resumeapp/Temp/Resume4.html')

def res5(request):
    return render(request,'Resumeapp/Temp/Resume5.html')

def login_page(request):
    if request.user.is_authenticated:
        return redirect("home/")
    else:
      if request.method=="POST":
        name=request.POST.get('username')
        pwd=request.POST.get('password')
        user=authenticate(request,username=name,password=pwd)
        if user is not None:
            login(request,user)
            messages.success(request,"Login  Succesfully")
            return redirect("home/")
        else:
            messages.error(request,"Invalid User Name or password")
    return render(request,"Resumeapp/login.html")


def register(request):
    form=CustomUserForm()
    if request.method=="POST":
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Success")
            return redirect('/')
    return render(request,"Resumeapp/register.html",{'form':form})

# def login_page(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             # Perform login logic
#             return redirect('home')  # Replace 'home' with the name of your homepage URL pattern
#     else:
#         form = AuthenticationForm()
#     return render(request, 'Resumeapp/login.html', {'form': form})
 
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request,"Registration Success")
#             return redirect('')
#     else:
#         form = UserCreationForm()
#     return render(request, 'Resumeapp/register.html', {'form': form})


def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out successfully")
    return redirect("/")
