from django.db import models

# Create your models here.
class Team(models.Model):
    team_id= models.IntegerField()
    team_name=models.CharField()
    established_date=models.DateField()

class Employee(models.Model):
    employee_id=models.IntegerField()
    last_name=models.CharField(max_length=255)
    first_name=models.CharField(max_length=255)
    title=models.CharField(max_length=255)
    start_date=models.DateField()
    end_date=models.DateField()
    salary=models.IntegerField()
    administrator=models.BooleanField()
    user_id=models.CharField(max_length=255)
    password=models.CharField(max_length=255)

class Athlete(models.Model):
    athlete_id=models.IntegerField()
    team_id=models.IntegerField()
    last_name=models.CharField(max_length=255)
    first_name=models.CharField(max_length=255)
    position=models.CharField(max_length=255)
    academic_level=models.IntegerField()
    contact=models.CharField(max_length=255)

class Scholarship(models.Model):
    scholarship_id=models.IntegerField()
    team_id=models.IntegerField()
    amount=models.IntegerField()
    date=models.DateField()
    donor=models.CharField(max_length=255)
    type=models.CharField(max_length=255)

class Rank(models.Model):
    rank_id=models.IntegerField()
    team_id=models.IntegerField()
    team_name=models.CharField(max_length=255)
    rank=models.IntegerField()
    record=models.IntegerField()

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
    event_id=models.IntegerField()
    team_id=models.IntegerField()
    date=models.DateField()
    income=models.IntegerField()
    expenses=models.IntegerField()
    opponent=models.CharField(max_length=255)

    