from django.shortcuts import render, redirect
from django.contrib.auth.forms import  UserCreationForm , AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import login
from django.views import View

#this views is function base we need class base viwes 
#im converting function base to class base 

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('/login') #in khat baraye redirect karadan safhe b login mibashad
            return HttpResponse('user has been created')



    form = UserCreationForm()
    return render(request, 'signup/signup.html',{'form':form})


class login(View):
    def login(request):
        if request == 'POST' :
            form = AuthenticationForm(data = request.POST)
            if form.is_valid():
                user = form.save()
                user = form.get_user()
                login(request, user)
                return redirect('/signup')
#bayad be 2 fanction tabdil shavad (get & post)

        form = AuthenticationForm()
        return render(request, 'signup/login.html',{'form':form})

