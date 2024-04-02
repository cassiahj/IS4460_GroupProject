from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from rest_framework import generics
from .models import Team, Athlete, Employee
from .forms import TeamForm, TeamCreateForm, TeamDeleteForm, EmployeeForm, EmployeeDeleteForm


class Home(View):
    def get(self, request):
        
        return render(request=request, template_name='home.html', context={})

class TeamList(View):

    def get(self,request):

        teams = Team.objects.all()

        return render(request = request,
                      template_name = 'team_list.html',
                      context = {'teams':teams})
    
class TeamAdd(View):

    

    def get(self, request):
        form = TeamCreateForm()
        return render(request=request, template_name='team_add.html', context={'form': form})

    def post(self, request):
        form = TeamCreateForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            return redirect('team-list')
        return render(request=request, template_name='team_add', context={'form': form})

class TeamEdit(View):
    def get(self,request,team_id):

        team = Team.objects.get(pk=team_id)
        form = TeamForm(instance=team)

        return render(request = request,
                      template_name = 'team_edit.html',
                      context = {'team':team,'form':form})
    
    def post(self,request,team_id):

        team = Team.objects.get(pk=team_id)
        form = TeamForm(request.POST,request.FILES,instance=team)

        if form.is_valid():
            
            team = form.save()
            return redirect('team-list')
        
        return render(request = request,
                      template_name = 'team_edit.html',
                      context = {'team':team,'form':form})
        
class TeamDelete(View):
    def get(self,request, team_id):
        team = Team.objects.get(pk=team_id)
        form = TeamDeleteForm(instance=team)
    
        return render(request = request,
                      template_name = 'team_delete.html',
                      context = {'team':team,'form':form})


    def post(self,request,team_id):
        team = Team.objects.get(pk = team_id)
        team.delete()
        return redirect('team-list')
     
class TeamDetails(View):
    def get(self, request, team_id):
        team = Team.objects.get(pk=team_id)
        fields = team._meta.get_fields()  

        return render(request=request, template_name='team_details.html', context={'team': team, 'fields': fields})


class EmployeeList(View):

    def get(self, request):

        employees = Employee.objects.all()

        return render(request=request,
                      template_name='employee_list.html',
                      context={'employees': employees})
class EmployeeAdd(View):

    def get(self, request):
        form = EmployeeForm()
        return render(request=request, template_name='employee_add.html', context={'form': form})

    def post(self, request):
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            return redirect('employee-list')
        return render(request=request, template_name='employee_add.html', context={'form': form})

class EmployeeEdit(View):
    def get(self, request, employee_id):

        employee = Employee.objects.get(pk=employee_id)
        form = EmployeeForm(instance=employee)

        return render(request=request,
                      template_name='employee_edit.html',
                      context={'employee': employee, 'form': form})

    def post(self, request, employee_id):

        employee = Employee.objects.get(pk=employee_id)
        form = EmployeeForm(request.POST, request.FILES, instance=employee)

        if form.is_valid():

            employee = form.save()
            return redirect('employee-list')

        return render(request=request,
                      template_name='employee_edit.html',
                      context={'employee': employee, 'form': form})

class EmployeeDelete(View):
    def get(self, request, employee_id):
        employee = Employee.objects.get(pk=employee_id)
        form = EmployeeDeleteForm(instance=employee)

        return render(request=request,
                      template_name='employee_delete.html',
                      context={'employee': employee, 'form': form})

    def post(self, request, employee_id):
        employee = Employee.objects.get(pk=employee_id)
        employee.delete()
        return redirect('employee-list')


class EmployeeDetails(View):
    def get(self, request, employee_id):
        employee = Employee.objects.get(pk=employee_id)
        fields = employee._meta.get_fields()

        return render(request=request,
                      template_name='employee_details.html',
                      context={'employee': employee, 'fields': fields})
    


    