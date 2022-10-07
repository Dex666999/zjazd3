from pprint import pprint

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from main.forms import ContactForm

# Create your views here.



def hello_world(request: HttpRequest):
    context = {}
    return render(request, 'main/hello.html', context)


def contact_us(request):
#     context = {'form': ContactForm()}
#     return render(request, 'main/contact_us.html', context)
#
# def contact(request):
   if request.method == "POST":
       form = ContactForm(data=request.POST)
       if form.is_valid():
           print(form.cleaned_data)
           return redirect('main:hello_world')
   else:
       print('invalid')
       form = ContactForm()
   return render(
       request,
       "main/contact_us.html",
       {"form": form}
   )
