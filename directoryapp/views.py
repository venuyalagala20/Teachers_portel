from django.shortcuts import render,redirect,get_object_or_404
from .models import Teacher
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm,EmployeeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# Create your views here.
@login_required
def home(request): 
	return render(request, 'home.html', {})

def login_user (request):
	if request.method == 'POST': #if someone fills out form , Post it 
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:# if user exist
			login(request, user)
			messages.success(request,('Youre logged in'))
			return redirect('home') #routes to 'home' on successful login  
		else:
			messages.success(request,('Error logging in'))
			return redirect('login') #re routes to login page upon unsucessful login
	else:
		return render(request, 'login.html', {})


@login_required
def logout_user(request):
	logout(request)
	messages.success(request,('Youre now logged out'))
	return redirect('/login')



def register_user(request):
	if request.method =='POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request,user)
			messages.success(request, ('Youre now registered'))
			return redirect('home')
	else: 
		form = SignUpForm() 

	context = {'form': form}
	return render(request, 'register.html', context)



class Teachers(LoginRequiredMixin,ListView):
 
    # specify the model for list view
    model = Teacher
    queryset = Teacher.objects.filter(LastName__startswith='S').values()
    template_name = "teachers.html"


class Teachersdetails(LoginRequiredMixin,DetailView):
    # specify the model to use
    model = Teacher
    template_name = "teacher_detail.html"

@login_required
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/emp')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form}) 







 