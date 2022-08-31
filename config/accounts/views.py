from ast import Num
import imp
from django.shortcuts import render, redirect
from django.contrib.auth.forms import  UserCreationForm , AuthenticationForm
from django.views import View
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from .models import phonenum
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


class signup(View):
    def get(self, request):
        return render(request, 'tmp/signup.html', {'form': UserCreationForm()})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/login')

        return render(request, 'tmp/signup.html', {'form': UserCreationForm()})

class Login(View):
    def get(self, request):
        return render(request, 'tmp/login.html', {'form': AuthenticationForm })

    def post(self, request):
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )

            if user is None :
                return render(

                    request,
                    'tmp/login.html',
                    { 'form': form, 'invalid_creds': True }

                )

            try:
                form.confirm_login_allowed(user)

            except ValidationError:

                return render(
                    request,
                    'tmp/login.html',
                    { 'form': form, 'invalid_creds': True }

                )


            return redirect('phonebook/')

def num(request):
    context = {
        'phonenums': phonenum.objects.all()
    }
    return render (request,'tmp/phonebook.html',context)


class SearchResultsView(ListView):
    model = phonenum
    template_name = 'tmp/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = phonenum.objects.filter(
            Q(name__icontains=query)
        )
        return object_list

def add(request):
    template = loader.get_template('tmp/add.html')
    return HttpResponse(template.render({}, request))


def addrecord(request):
    x = request.POST['first']
    y = request.POST['number']
    Phonenum = phonenum(name = x, phone_num = y)
    Phonenum.save()
    return HttpResponseRedirect(reverse('phonebook'))