from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
	path('',views.myQuizApp,name="quiz-home"),
	path('register',views.register,name='quiz-registration'),
	path('loginUser',views.loginUser,name='login'),
	path('index',views.index,name='quiz-test'),
	path('quiz/<int:myid>',views.quiz,name='quiz'),
	path('quiz/logout',views.logoutUser,name='logout'),
	path('logout',views.logoutUser,name='logout'),
	path('quiz/result/<int:user_id>',views.result,name='result'),
	path('scoreboard',views.scoreboard,name='scoreboard'),
	path('quiz/result/score',views.score,name='score'),
	path('quiz/saveans',views.saveans,name='saveans'),
	path('quiz/result/index',views.index,name='quiz-test'),
	path('quiz/result/logout',views.logoutUser,name='logout'),
	path('quiz/result/myQuizApp',views.myQuizApp,name='quiz-home'),
	
]
