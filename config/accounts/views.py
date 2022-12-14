from django.shortcuts import render, redirect
from django.contrib.auth.forms import  UserCreationForm , AuthenticationForm
from django.views import View
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from .models import phonenum
from django.views.generic import ListView
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


class signup(View):
    form_class = UserCreationForm

    def get(self, request):
        form = self.form_class
        return render(request, 'tmp/signup.html', {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/')

        return render(request, 'tmp/signup.html', {'form':form})

class Login(View):
    form_class = AuthenticationForm

    def get(self, request):
        return render(request, 'tmp/login.html', {'form': self.form_class })

    def post(self, request):
        form = self.form_class(request, data = request.POST)
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
        
        return render (request,'tmp/login.html',{
        'help_text': True, 
        'form': AuthenticationForm
        })

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
    y = request.POST['last']
    Phonenum = phonenum(name = x, phone_num = y)
    Phonenum.save()
    return HttpResponseRedirect(reverse('phonebook'))



def delete(request, id):
  Phonenum = phonenum.objects.get(id = id)
  Phonenum.delete()
  return HttpResponseRedirect(reverse('phonebook'))

def update(request, id):
  mymember = phonenum.objects.get(id = id)
  template = loader.get_template('tmp/update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  Phonenum = phonenum.objects.get(id=id)
  Phonenum.name = first
  Phonenum.phone_num = last
  Phonenum.save()
  return HttpResponseRedirect(reverse('phonebook'))