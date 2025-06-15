from django import forms
from .models import Method,Man,Machine,Material,Shift,MachineUsage
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ManForm(forms.ModelForm):
    class Meta:
        model = Man
        fields = ['name','email','phone_no','role', 'shift']


class MethodForm(forms.ModelForm):
    class Meta:
        model = Method
        fields = ['name', 'description', 'machines', 'materials']
        widgets = {
            'machines': forms.CheckboxSelectMultiple(),
            'materials': forms.CheckboxSelectMultiple(),
        }

class AssignMachineForm(forms.ModelForm):
    class Meta:
        model = Man
        fields = ['machines']
        widgets = {'machines': forms.CheckboxSelectMultiple}

class MachineForm(forms.ModelForm):
    class Meta:
        model= Machine
        fields= ['name','type','status']
        widgets = {
            'type': forms.Select(),
            'status': forms.Select(),
        }

class MaterialForm(forms.ModelForm):
    class Meta:
        model= Material
        fields=['name','category']
        widgets={
            'category':forms.Select()
        }

class ShiftForm(forms.ModelForm):
    class Meta:
        model=Shift
        fields=['name','start_time','end_time']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }

class MachineUsageForm(forms.ModelForm):
    class Meta:
        model=MachineUsage
        model = MachineUsage
        fields = ['man', 'machine', 'method', 'start_time', 'end_time']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }