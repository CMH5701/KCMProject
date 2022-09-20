import imp
from django.shortcuts import render,redirect,get_object_or_404
from kcmapp.forms import CashbookForm
from django.utils import timezone
from .models import Cashbook

# Create your views here.

def main(request):
    return render(request , 'main.html')

def write(request) :
    if request.method == 'POST':
        form = CashbookForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now() 
            form.save()
            return redirect('main')

    else:
        form = CashbookForm
        return render(request, 'write.html', {'form':form})

def read(request) :
    cashbooks = Cashbook.objects.all()
    return render(request, 'read.html', {'cashbooks':cashbooks})

def detail(request,id) :
        cashbooks = get_object_or_404(Cashbook, id=id)
        return render(request, 'detail.html', {'cashbooks':cashbooks})