from django.urls import path
from .import views
urlpatterns=[
    path('',views.sample,name="nibbi"),
    path('signin/',views.sample1,name='signin'),
    path('register/',views.sample2,name='register'),
    path('getres/',views.getres,name='getres'),
    path('signuppost/',views.signuppost,name="spost"),
    path("recovery/",views.recovery,name="recovery"),
    path("forgot1/",views.forgot1,name="frr"),
    path("updatepass/",views.checknewpass,name="checknew"),
    path("recoverypass/",views.recoverypass,name="rer"),

]

