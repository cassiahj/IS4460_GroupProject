from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


from .models import Team, Athlete, Employee, Event, Equipment, Scholarship, Income, Rank
from .forms import TeamForm, TeamCreateForm, TeamDeleteForm, EmployeeForm, EmployeeDeleteForm, AthleteForm, EventForm, EquipmentForm, ScholarshipForm, IncomeForm, RankForm


class Home(LoginRequiredMixin, View):
    def get(self, request):
        
        return render(request=request, template_name='home.html', context={})
    

# class ReportList(View):
#     def get(self, request):

#         teams = Team.objects.all()
#         return render(request = request, template_name = 'report_list.html', context = {})

def can_view_reports(request):
    return request.user.groups.filter(name='Admin').exists()


class Report(LoginRequiredMixin, View):
    def get(self, request, team_id):
        user_message = ""
        team = None
        employees = None
        athletes = None
        scholarships = None
        incomes = None
        equipments = None
        events = None
        if not can_view_reports(request):
            user_message = "Cannot View Reports. You are an employee not an admin."
        else: 
            team = Team.objects.get(pk=team_id)
            employees = team.employees.all()
            athletes = team.athletes.all()
            scholarships = Scholarship.objects.filter(athlete__in=athletes)
            incomes = Income.objects.filter(team=team)
            equipments = Equipment.objects.filter(team=team)
            events = Event.objects.filter(team=team)


      
        return render(request = request,
                    template_name = 'report.html',
                    context = { 'team': team,
                                'employees': employees,
                                'athletes' : athletes,
                                'scholarships': scholarships,
                                'incomes': incomes,
                                'equipments': equipments,
                                'events': events,
                                'user_message': user_message
                                })


class TeamList(View):

    def get(self,request):

        teams = Team.objects.all()

        return render(request = request,
                      template_name = 'team_list.html',
                      context = {'teams':teams})
    
class TeamAdd( CreateView):

    model = Team
    form_class = TeamForm
    template_name = 'team_add.html'
    success_url = '/athletics/team/list/'


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
    
class AthleteAdd(CreateView):
    model = Athlete
    form_class = AthleteForm
    template_name = 'athlete_add.html'
    success_url = '/athletics/athlete/list/'


class AthleteList(ListView):
    model = Athlete
    template_name = 'athlete_list.html'
    context_object_name = 'athletes'

class AthleteDelete(DeleteView):
    model = Athlete
    success_url = reverse_lazy('athlete-list')
    template_name = 'athlete_delete.html'

class AthleteDetails(DetailView):
    model = Athlete
    template_name = 'athlete_details.html'

class AthleteEdit(UpdateView):
    model = Athlete
    form_class = AthleteForm
    template_name = 'athlete_edit.html'
    success_url = reverse_lazy('athlete-list')

class EventAdd(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'event_add.html'
    success_url = '/athletics/event/list/'

class EventList(ListView):
    model = Event
    template_name = 'event_list.html'
    context_object_name = 'events'

class EventDelete(DeleteView):
    model = Event
    success_url = reverse_lazy('event-list')
    template_name = 'event_delete.html'

class EventDetails(DetailView):
    model = Event
    template_name = 'event_details.html'

class EventEdit(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'event_edit.html'
    success_url = reverse_lazy('event-list')
    

class EquipmentAdd(CreateView):
    model = Equipment
    form_class = EquipmentForm
    template_name = 'equipment_add.html'
    success_url = '/athletics/equipment/list/'

class EquipmentList(ListView):
    model = Equipment
    template_name = 'equipment_list.html'
    context_object_name = 'equipment'

class EquipmentDelete(DeleteView):
    model = Equipment
    success_url = reverse_lazy('equipment-list')
    template_name = 'equipment_delete.html'

class EquipmentDetails(DetailView):
    model = Equipment
    template_name = 'equipment_details.html'

class EquipmentEdit(UpdateView):
    model = Equipment
    form_class = EquipmentForm
    template_name = 'equipment_edit.html'
    success_url = reverse_lazy('equipment-list')

class ScholarshipAdd(CreateView):
    model = Scholarship
    form_class = ScholarshipForm
    template_name = 'scholarship_add.html'
    success_url = '/athletics/scholarship/list/'

class ScholarshipList(ListView):
    model = Scholarship
    template_name = 'scholarship_list.html'
    context_object_name = 'scholarships'

class ScholarshipDelete(DeleteView):
    model = Scholarship
    success_url = reverse_lazy('scholarship-list')
    template_name = 'scholarship_delete.html'

class ScholarshipDetails(DetailView):
    model = Scholarship
    template_name = 'scholarship_details.html'

class ScholarshipEdit(UpdateView):
    model = Scholarship
    form_class = ScholarshipForm
    template_name = 'scholarship_edit.html'
    success_url = reverse_lazy('scholarship-list')

class IncomeAdd(CreateView):
    model = Income
    form_class = IncomeForm
    template_name = 'income_add.html'
    success_url = '/athletics/income/list/'

class IncomeList(ListView):
    model = Income
    template_name = 'income_list.html'
    context_object_name = 'incomes'

class IncomeDelete(DeleteView):
    model = Income
    success_url = reverse_lazy('income-list')
    template_name = 'income_delete.html'

class IncomeDetails(DetailView):
    model = Income
    template_name = 'income_details.html'

class IncomeEdit(UpdateView):
    model = Income
    form_class = IncomeForm
    template_name = 'income_edit.html'
    success_url = reverse_lazy('income-list')
# 

# class RankAdd(CreateView):
#     model = Rank
#     form_class = RankForm
#     template_name = 'rank_add.html'
#     success_url = '/athletics/rank/list/'

# class RankList(ListView):
#     model = Rank
#     template_name = 'rank_list.html'
#     context_object_name = 'ranks'

# class RankDelete(DeleteView):
#     model = Rank
#     success_url = reverse_lazy('rank-list')
#     template_name = 'rank_delete.html'

# class RankDetails(DetailView):
#     model = Rank
#     template_name = 'rank_details.html'

# class RankEdit(UpdateView):
#     model = Rank
#     form_class = RankForm
#     template_name = 'rank_edit.html'
    # success_url = reverse_lazy('rank-list')

