import os
import django
import random
from datetime import datetime, timedelta


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_project.settings')
django.setup()

from athletics.models import Team, Employee, Athlete, Scholarship, Income, Equipment, Event, Rank

# Function to generate random date within a range
def random_date(start_date, end_date):
    return start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))

# Function to generate semi-realistic data for teams
def populate_teams(num_teams):
    for i in range(num_teams):
        Team.objects.create(
            team_name=f"Team {i+1}",
            type=random.choice(['Football', 'Basketball', 'Soccer', 'Volleyball', 'Track and Field']),
            email=f"team{i+1}@utah.edu",
            established_date=random_date(datetime(2000, 1, 1), datetime.now())
        )

# Function to generate semi-realistic data for employees
def populate_employees(num_employees):
    for i in range(num_employees):
        Employee.objects.create(
            first_name=f"Employee{i+1}",
            last_name=f"Lastname{i+1}",
            title=random.choice(['Coach', 'Trainer', 'Administrator']),
            start_date=random_date(datetime(2010, 1, 1), datetime.now()),
            end_date=random_date(datetime(2020, 1, 1), datetime.now()),
            salary=random.randint(40000, 200000),  
            administrator=random.choice([True, False]),
            user_id=f"user{i+1}",
            password=f"password{i+1}"
        )

# Function to generate semi-realistic data for athletes
def populate_athletes(num_athletes):
    for i in range(num_athletes):
        Athlete.objects.create(
            first_name=f"Athlete{i+1}",
            last_name=f"Lastname{i+1}",
            position=random.choice(['Forward', 'Guard', 'Center', 'Goalkeeper', 'Striker', 'Midfielder']),
            academic_level=random.choice(['FR', 'SO', 'JR', 'SR', 'OT']),
            contact=f"+123456789{i+1}"
        )

# Function to generate semi-realistic data for scholarships
def populate_scholarships(num_scholarships):
    athletes = Athlete.objects.all()
    for i in range(num_scholarships):
        athlete = athletes[random.randint(0, len(athletes) - 1)]
        Scholarship.objects.create(
            athlete=athlete,
            amount=random.randint(1000, 50000),
            date_awarded=random_date(datetime(2010, 1, 1), datetime.now()),
            donor=f"Donor {i+1}",
            type=random.choice(['Academic', 'Athletic', 'Financial Need', 'Other'])
        )

# Function to generate semi-realistic data for incomes
def populate_incomes(num_incomes):
    teams = Team.objects.all()
    for i in range(num_incomes):
        team = teams[random.randint(0, len(teams) - 1)]
        Income.objects.create(
            team=team,
            type=random.choice(['Donation', 'State', 'University', 'TV Network', 'Event Payout']),
            amount=random.randint(1000, 100000),  
            date_recorded=random_date(datetime(2010, 1, 1), datetime.now())
        )

# Function to generate semi-realistic data for equipment
def populate_equipment(num_equipment):
    teams = Team.objects.all()
    for i in range(num_equipment):
        team = teams[random.randint(0, len(teams) - 1)]
        Equipment.objects.create(
            team=team,
            type=random.choice(['Jerseys', 'Balls', 'Shoes', 'Training Gear']),
            notes=f"Notes for equipment {i+1}",
            upfront_cost=random.randint(100, 5000),
            annual_cost=random.randint(100, 2000),  
            date_purchased=random_date(datetime(2010, 1, 1), datetime.now())
        )

# Function to generate semi-realistic data for events
def populate_events(num_events):
    teams = Team.objects.all()
    for i in range(num_events):
        team = teams[random.randint(0, len(teams) - 1)]
        Event.objects.create(
            name=f"Event {i+1}",
            team=team,
            income=random.randint(1000, 100000),  
            date=random_date(datetime(2010, 1, 1), datetime.now()),
            expenses=random.randint(500, 50000),  
            opponent=f"Opponent {i+1}"
        )

# Function to generate semi-realistic data for ranks
def populate_ranks(num_ranks):
    teams = Team.objects.all()
    for i in range(num_ranks):
        team = teams[random.randint(0, len(teams) - 1)]
        Rank.objects.create(
            team=team,
            rank=random.randint(1, 25),
            date_recorded=random_date(datetime(2010, 1, 1), datetime.now())
        )

if __name__ == '__main__':
    populate_teams(20)
    populate_employees(20)
    populate_athletes(20)
    populate_scholarships(20)
    populate_incomes(20)
    populate_equipment(20)
    populate_events(20)
    populate_ranks(20)
