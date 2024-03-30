from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from rest_framework import generics
from .models import Team, Athlete
from .forms import TeamForm, TeamCreateForm, TeamDeleteForm

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


class Home(View):
    def get(self, request):
        
        return render(request=request, template_name='home.html', context={})


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


