from django.shortcuts import render
from .models import TeamMember
import requests

def our_team(request):
    team_members = TeamMember.objects.all()
    return render(request, 'team/our_team.html', {'team_members': team_members})
