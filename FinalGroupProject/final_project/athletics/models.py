from django.db import models



#attempted M:N relationships for team/employee, team/athlete

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    established_date = models.DateField()
    employees = models.ManyToManyField('Employee', related_name='teams')

    def __str__(self):
        return self.team_name

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    salary = models.IntegerField()
    administrator = models.BooleanField()
    user_id = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Athlete(models.Model):
    ACADEMIC_LEVEL_CHOICES = [
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('OT', 'Other'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    position = models.CharField(max_length=255)
    academic_level = models.CharField(max_length=2, choices=ACADEMIC_LEVEL_CHOICES)
    contact = models.CharField(max_length=255)
    teams = models.ManyToManyField('Team', related_name='athletes')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"




class Scholarship(models.Model):
    scholarship_id=models.IntegerField()
    team_id=models.IntegerField()
    amount=models.IntegerField()
    date=models.DateField()
    donor=models.CharField(max_length=255)
    type=models.CharField(max_length=255)

# class Rank(models.Model):
#     rank_id=models.IntegerField()
#     team_id=models.IntegerField()
#     team_name=models.CharField(max_length=255)
#     rank=models.IntegerField()
#     record=models.IntegerField()

class Income(models.Model):
    income_id=models.IntegerField()
    team_id=models.IntegerField()
    type=models.CharField(max_length=255)
    amount=models.DateField()

class Equipment(models.Model):
    equipment_id=models.IntegerField()
    team_id=models.IntegerField()
    type=models.TextField()
    annual_cost=models.IntegerField()
    year=models.DateField()

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    income = models.IntegerField()
    date = models.DateField()
    expenses = models.IntegerField()
    opponent = models.CharField(max_length=255)
