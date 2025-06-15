from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Shift(models.Model):
    name=models.CharField(max_length=100)
    start_time=models.TimeField()
    end_time=models.TimeField()

    def __str__(self):
        return self.name

class Man(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone_no=models.CharField(max_length=15)
    role = models.CharField(max_length=50)
    shift = models.ForeignKey(Shift, on_delete=models.SET_NULL, null=True, related_name='men')
    machines = models.ManyToManyField('Machine', blank=True, related_name='men')
    
    def __str__(self):
        return self.name

class Machine(models.Model):
    TYPE_CHOICES = [
        ('welder', 'Welding Machine'),
        ('milling', 'Milling Machine'),
        ('drill', 'Drill'),
    ]
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('maintenance', 'Maintenance'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    def __str__(self):
        return self.name
    
class Material(models.Model):
    CATEGORY_CHOICES = [
        ('metal', 'Metal'),
        ('plastic', 'Plastic'),
        ('wood', 'Wood'),
        ('glass', 'Glass'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    
    def __str__(self):
        return self.name

class Method(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    responsible_man = models.ForeignKey(Man, on_delete=models.SET_NULL, null=True, related_name='methods')
    machines = models.ManyToManyField(Machine)
    materials = models.ManyToManyField(Material)

    def __str__(self):
        return self.name
    
class MachineUsage(models.Model):
    man = models.ForeignKey(Man, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    method = models.ForeignKey(Method, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.man.name} - {self.machine.name}"