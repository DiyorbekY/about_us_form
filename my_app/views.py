from django.http import HttpResponse
from .models import Countries,Employees,Jobs
from django.db.models import Count

def my_list(request):
    # queryset = Employees.objects.filter(Q(first_name__endswith='a') & Q(last_name__endswith='z'))
    # print(queryset.query)
    # country_list = ""
    # for c in queryset:
    #     country_list += f"<li>{c.first_name} {c.last_name}</li>"
    # return HttpResponse(f"<ol>{country_list}</ol>")
    # queryset=Jobs.objects.prefetch_related('employees_set').annotate(soni=Count('job_id'))
    # print(queryset.query)
    # country_list=''
    # for c in queryset:
    #     country_list += f"<li>{c}</li>"
    # return HttpResponse(f"<ol>{country_list}</ol>")

    queryset = Jobs.objects.annotate(employee_soni=Count('employees'))
    country_list = ''
    for c in queryset:
        country_list += f"<li>{c.job_title} — {c.employee_soni} ta xodim</li>"

    return HttpResponse(f"<ol>{country_list}</ol>")
