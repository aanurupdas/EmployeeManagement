from django.urls import path
from .views import EmployeeList,EmployeeCreate,EmployeeUpdate,EmployeeDelete
from .views import DepartmentList,DepartmentCreate,DepartmentUpdate,DepartmentDelete


urlpatterns = [
    path('', DepartmentList.as_view(), name='department'),
    path('department-create', DepartmentCreate.as_view(), name='department-create'),
    path('department-update/<int:pk>', DepartmentUpdate.as_view(), name='department-update'),
    path('department-delete/<int:pk>', DepartmentDelete.as_view(), name='department-delete'),

    path('employee', EmployeeList.as_view(), name='employee'),
    path('employee-create', EmployeeCreate.as_view(), name='employee-create'),
    path('employee-update/<int:pk>', EmployeeUpdate.as_view(), name='employee-update'),
    path('employee-delete/<int:pk>', EmployeeDelete.as_view(), name='employee-delete'),
]