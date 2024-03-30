from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home/',views.Home.as_view(),name = 'home'),
    path('list/', views.TeamList.as_view(),name = 'team-list'),
    path('add/', views.TeamAdd.as_view(), name = 'team-add'),
    path('edit/<int:team_id>/', views.TeamEdit.as_view(),name = 'team-edit'),
    path('delete/<int:team_id>/', views.TeamDelete.as_view(),name = 'team-delete'),
    path('details/<int:team_id>/', views.TeamDetails.as_view(), name = 'team-details')
]