from django.urls import path, include 
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home/',views.Home.as_view(),name = 'home'),
    path('athletics/', include("django.contrib.auth.urls")),

    path('team/list/', views.TeamList.as_view(),name = 'team-list'),
    path('team/add/', views.TeamAdd.as_view(), name = 'team-add'),
    path('team/edit/<int:team_id>/', views.TeamEdit.as_view(),name = 'team-edit'),
    path('team/delete/<int:team_id>/', views.TeamDelete.as_view(),name = 'team-delete'),
    path('team/details/<int:team_id>/', views.TeamDetails.as_view(), name = 'team-details'),
    
    path('employee/list/', views.EmployeeList.as_view(),name='employee-list'),
    path('employee/add/', views.EmployeeAdd.as_view(), name='employee-add'),
    path('employee/edit/<int:employee_id>/', views.EmployeeEdit.as_view(),name='employee-edit'),
    path('employee/delete/<int:employee_id>/', views.EmployeeDelete.as_view(),name='employee-delete'),
    path('employee/details/<int:employee_id>/', views.EmployeeDetails.as_view(), name='employee-details'),

    path('athlete/list/', views.AthleteList.as_view(), name='athlete-list'),
    path('athlete/add/', views.AthleteAdd.as_view(), name='athlete-add'),
    path('athlete/edit/<int:pk>/', views.AthleteEdit.as_view(), name='athlete-edit'),
    path('athlete/delete/<int:pk>/', views.AthleteDelete.as_view(), name='athlete-delete'),
    path('athlete/details/<int:pk>/', views.AthleteDetails.as_view(), name='athlete-details'),

    path('event/list/', views.EventList.as_view(), name='event-list'),
    path('event/add/', views.EventAdd.as_view(), name='event-add'),
    path('event/edit/<int:pk>/', views.EventEdit.as_view(), name='event-edit'),
    path('event/delete/<int:pk>/', views.EventDelete.as_view(), name='event-delete'),
    path('event/details/<int:pk>/', views.EventDetails.as_view(), name='event-details'),

    path('equipment/list/', views.EquipmentList.as_view(), name='equipment-list'),
    path('equipment/add/', views.EquipmentAdd.as_view(), name='equipment-add'),
    path('equipment/edit/<int:pk>/', views.EquipmentEdit.as_view(), name='equipment-edit'),
    path('equipment/delete/<int:pk>/', views.EquipmentDelete.as_view(), name='equipment-delete'),
    path('equipment/details/<int:pk>/', views.EquipmentDetails.as_view(), name='equipment-details'),

    path('scholarship/list/', views.ScholarshipList.as_view(), name='scholarship-list'),
    path('scholarship/add/', views.ScholarshipAdd.as_view(), name='scholarship-add'),
    path('scholarship/edit/<int:pk>/', views.ScholarshipEdit.as_view(), name='scholarship-edit'),
    path('scholarship/delete/<int:pk>/', views.ScholarshipDelete.as_view(), name='scholarship-delete'),
    path('scholarship/details/<int:pk>/', views.ScholarshipDetails.as_view(), name='scholarship-details'),

    path('income/list/', views.IncomeList.as_view(), name='income-list'),
    path('income/add/', views.IncomeAdd.as_view(), name='income-add'),
    path('income/edit/<int:pk>/', views.IncomeEdit.as_view(), name='income-edit'),
    path('income/delete/<int:pk>/', views.IncomeDelete.as_view(), name='income-delete'),
    path('income/details/<int:pk>/', views.IncomeDetails.as_view(), name='income-details'),

]
