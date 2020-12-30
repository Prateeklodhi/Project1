from django.shortcuts import render,redirect
from .models import Client
from .form import ClientForm
from django.contrib import messages

# Create your views here.
def  index(request):
    form = ClientForm()
    
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Thanks for your details. We will contect you soon...")
            return redirect('/')    
        else :
            messages.error(request,"Something is worng. check your given details please..")
            return redirect('/')

    context ={
        'form':form
    }
    return render(request,'index.html',context)