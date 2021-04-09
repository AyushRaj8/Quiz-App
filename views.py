from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Quiz, Question, CreateUserForm, QuizTaker
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator

l=[]
al=[]
score=0

def myQuizApp(request):
	quiz = Quiz.objects.all()
	return render(request,"home.html",{"title":'myQuizApp','quiz':quiz})
	
def register(request):
	reg_form=CreateUserForm()
	if request.method=='POST':
		reg_form = CreateUserForm(request.POST);
		if reg_form.is_valid():
			reg_form.save()
			messages.success(request,'Account created')
			reg_form = CreateUserForm();
			return render(request,'register.html',{'reg_form':reg_form})
		else:
			return render(request,'register.html',{'reg_form':reg_form})
	else:
		reg_form = CreateUserForm();
		return render(request,'register.html',{'reg_form':reg_form})
		
def loginUser(request):
	if request.method == "POST":
		username = request.POST.get('username') 
		password = request.POST.get('password')
		#check if user has entered correct credentials
		user = authenticate(username=username, password=password)
		if user is not None:
		# A backend authenticated the credentials
			login(request, user)
			messages.success(request, "Logged in successfully!")
			return redirect("/myQuizApp")
		else:
           	 # No backend authenticated the credentials
			messages.warning(request, "Wrong Username or Password. Try Again")
			return render(request, 'login.html')
	return render(request, 'login.html')
    
def logoutUser(request):
    	logout(request)
    	messages.info(request, 'You have been logged out.')
    	return redirect("/myQuizApp")
    
def index(request):
	quizes = Quiz.objects.all()
	params = {'quiz':quizes,'title': 'Test Section'}
	l.clear()
	al.clear()
	return render(request,'index.html',params)
	
def quiz(request,myid):
	if request.user.is_anonymous:
		return redirect("login")
	obj = Question.objects.filter(quiz_id = myid)
	for i in obj:
		al.append(i.ans)
	paginator = Paginator(obj,1)
	try:
		page = int(request.GET.get('page','1'))
	except:
		page = 1
	try :
		questions = paginator.page(page)
	except(EmptyPage,InvalidPage):
		questions = paginator.page(paginator.num_pages)
	return render (request,'quiz.html',{'obj':obj,'questions':questions,'title':'Test'})

def score(request):
	return render(request,'scoreboard.html')
	
def saveans(request):
    	ans = request.GET['ans']
    	l.append(ans)
    	return render(request, 'result.html')

def result(request, user_id):
	score = 0
	for i in range(len(l)):
		if l[i] == al[i]:
			score += 1
	score = (score/len(l))*100
	user = User.objects.get(id = user_id)
	obj = QuizTaker.objects.create(
		user_name = user,
		score = score
	)
	return render(request, 'result.html', {"score": score})
	
def scoreboard(request):
	users = QuizTaker.objects.all()
	return render(request, 'scoreboard.html', {"users": users})
	
