from django import forms
from .models import Skill
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'proficiency']
        
    def clean_proficiency(self):
        proficiency = self.cleaned_data.get('proficiency')
        if proficiency < 0 or proficiency > 100:
            raise forms.ValidationError("Proficiency must be between 0 and 100.")
        return proficiency

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Skill.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError("This skill already exists.")
        return name

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
