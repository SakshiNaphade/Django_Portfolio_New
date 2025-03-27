from django.shortcuts import redirect, render
from .models import Skill
from .forms import SkillForm
import json
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def projects(request):
    return render(request, 'main/projects.html')

def contact(request):
    return render(request, 'main/contact.html')

@login_required
def dashboard(request):
    skills = Skill.objects.all()
    chart_data = {
        "labels": [skill.name for skill in skills],
        "data": [skill.proficiency for skill in skills]
    }

    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Refresh the page after adding skill
    else:
        form = SkillForm()

    return render(request, 'main/dashboard.html', {'chart_data': json.dumps(chart_data), 'form': form})
    skills = Skill.objects.all()
    chart_data = {
        "labels": [skill.name for skill in skills],
        "data": [skill.proficiency for skill in skills]
    }

    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Refresh the page after adding skill
    else:
        form = SkillForm()
    
    #return render(request, 'main/dashboard.html', {'chart_data': json.dumps(chart_data), 'form': form})
    return render(request, 'main/dashboard.html', {'chart_data': chart_data})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form})

