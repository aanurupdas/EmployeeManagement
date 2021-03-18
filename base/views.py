from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Department,Employee

#############################Department#############################
class DepartmentList(ListView):
    model = Department
    template_name = 'department/department_list.html'
    context_object_name = 'departments'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = context['departments'].all()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['departments'] = context['departments'].filter(
                name__icontains=search_input)

        context['search_input'] = search_input

        return context

class DepartmentCreate(CreateView):
    model = Department
    template_name = 'department/department_form.html'
    fields = ['name']
    success_url = reverse_lazy('department')
    
    def form_valid(self, form):    
        return super(DepartmentCreate, self).form_valid(form)

class DepartmentUpdate(UpdateView):
    model = Department
    template_name = 'department/department_form.html'
    fields = ['name']
    success_url = reverse_lazy('department')

class DepartmentDelete(DeleteView):
    model = Department
    template_name = 'department/department_confirm_delete.html'
    context_object_name = 'department'
    success_url = reverse_lazy('department')

###########################Employee##########################
class EmployeeList(ListView):
    model = Employee
    template_name = 'employee/employee_list.html'
    context_object_name = 'employees'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['employees'] = context['employees'].all()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['employees'] = context['employees'].filter(
                name__icontains=search_input)

        context['search_input'] = search_input

        return context

class EmployeeCreate(CreateView):
    model = Employee
    template_name = 'employee/employee_form.html'
    fields = ['image','name','email','department']
    success_url = reverse_lazy('employee')
    
    def form_valid(self, form):    
        return super(EmployeeCreate, self).form_valid(form)

class EmployeeUpdate(UpdateView):
    model = Employee
    template_name = 'employee/employee_form.html'
    fields = ['image','name','email','department']
    success_url = reverse_lazy('employee')

class EmployeeDelete(DeleteView):
    model = Employee
    template_name = 'employee/employee_confirm_delete.html'
    context_object_name = 'employee'
    success_url = reverse_lazy('employee')
