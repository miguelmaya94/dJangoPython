from django.shortcuts import render
from django.http import HttpResponse
from .models import Members
from .forms import MemberForm

# Create your views here.

   

def say_hello(request):
    all_members = Members.objects.all
    return render(request, 'index.html', {'all':all_members})

def join(request):
    if request.method == "POST":
        form = MemberForm(request.POST or 'NONE')
        if form.is_valid():
            form.save()
        return render(request, 'join.html', {})
    else:
        return render(request, 'join.html', {})
    
def joins(request):
      return render(request, 'join.html')