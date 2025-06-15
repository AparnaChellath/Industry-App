from django.contrib import admin
from .models import Shift, Man,Machine,Material,MachineUsage
from .models import Machine
# Register your models here.

class MachineUsageInline(admin.TabularInline): 
    model = MachineUsage
    extra = 1  
    readonly_fields = ['start_time', 'end_time']

class MachineAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'status']  
    list_filter = ['type', 'status'] 
    inlines = [MachineUsageInline]

# admin.site.register(Machine)
admin.site.register(Material)
admin.site.register(Shift)
admin.site.register(Man)
admin.site.register(Machine, MachineAdmin)

