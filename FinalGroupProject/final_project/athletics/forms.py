from django import forms
from athletics.models import Team,Employee, Athlete, Event, Equipment
from datetime import date

class TeamCreateForm(forms.ModelForm):
    class Meta:
        model = Team
        exclude = ['team_id','established_date']

    def save(self, commit=True):
        instance = super(TeamForm, self).save(commit=False)
        instance.established_date = date.today()
        if commit:
            instance.save()
        return instance
    

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

class TeamDeleteForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('team_name',)


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class EmployeeDeleteForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('employee_id','first_name', 'last_name',)


class AthleteForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = '__all__'
        
        
class AthleteDeleteForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = ('id', 'first_name', 'last_name',)


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
        
class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'

        widgets = {
            'date_purchased': forms.DateInput(attrs={'type': 'date'}),

        }
        
