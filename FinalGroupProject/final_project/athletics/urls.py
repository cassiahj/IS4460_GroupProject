from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home/',views.Home.as_view(),name = 'home'),
    path('team/list/', views.TeamList.as_view(),name = 'team-list'),
    path('team/add/', views.TeamAdd.as_view(), name = 'team-add'),
    path('team/edit/<int:team_id>/', views.TeamEdit.as_view(),name = 'team-edit'),
    path('team/delete/<int:team_id>/', views.TeamDelete.as_view(),name = 'team-delete'),
    path('team/details/<int:team_id>/', views.TeamDetails.as_view(), name = 'team-details'),
    
    path('employee/list/', views.EmployeeList.as_view(),name='employee-list'),
    path('employee/add/', views.EmployeeAdd.as_view(), name='employee-add'),
    path('employee/edit/<int:employee_id>/', views.EmployeeEdit.as_view(),name='employee-edit'),
    path('employee/delete/<int:employee_id>/', views.EmployeeDelete.as_view(),name='employee-delete'),
    path('employee/details/<int:employee_id>/', views.EmployeeDetails.as_view(), name='employee-details')
]