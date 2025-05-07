from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Regions, Countries, Locations, Departments, Jobs, Employees, Dependents

admin.site.register(Regions)
admin.site.register(Countries)
admin.site.register(Locations)
admin.site.register(Departments)
admin.site.register(Jobs)
admin.site.register(Employees)
admin.site.register(Dependents)