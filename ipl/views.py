from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Matches
from django.views.generic import TemplateView


@api_view(['GET'])
def get_batting(request):
    """ Percentage of teams decided to bat when won the toss """
    season = request.query_params['season']
    if season:
        query = Matches.objects.filter(season=season).filter(toss_decision='bat').count()
        query_2 = Matches.objects.filter(season=season).count()
        try:
            batting_per = round((query / query_2) * 100, 2)
            print(batting_per)
            return Response(batting_per)
        except:
            return query


@api_view(['GET'])
def get_most_matches(request):
    season = request.query_params['season']
    if season:
        query = Matches.objects.filter(season=season).values('venue').order_by('venue').annotate(Count('venue'))
        print(query)
        query_2 = Matches.objects.filter(season=season).count()

        return Response(query)





