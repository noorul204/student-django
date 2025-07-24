from django.shortcuts import render, redirect
from .models import Skill
from .forms import SkillForm
from django.contrib.auth.decorators import login_required



@login_required
def dashboard(request):
    skills = Skill.objects.filter(user=request.user)
    return render(request, 'tracker/dashboard.html', {'skills': skills})

@login_required
def add_skill(request):
    form = SkillForm(request.POST or None)
    if form.is_valid():
        skill = form.save(commit=False)
        skill.user = request.user
        skill.save()
        return redirect('dashboard')
    return render(request, 'tracker/add_skill.html', {'form': form})
