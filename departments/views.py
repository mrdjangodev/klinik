from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Department
# Create your views here.

def main_index(request):
    departments = Department.objects.all()
    search_data = request.POST.get('search_input')
    if search_data:
        departments = Department.objects.filter(name__icontains=search_data)
    paginator = Paginator(departments, 1)  # Show 10 departments per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_data': search_data,
    }   
  
    return render(request, "departments/main_index.html", context)


def main_index2(request):
    context = {

    }
    return render(request, "departments/index3.html", context)

def department_detail(request, pk:int):
    department = get_object_or_404(Department, id=pk)
    context = {
        'department': department,    
    }
    return render(request, 'departments/single_department.html', context)


