from .models import Matches, Delivery
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from .serializers import MatchSerializer, TossSerializer, YearSerializer, PlayerOfMatchSerializer, \
    MaxMatchSerializer, LocationSerializer, HighestMarginRunSerializer,HighestMarginWicketsSerializer,\
    TossWinnerSerializer


class MatchAPI(ModelViewSet):
    """ API for top 4 teams in a season """
    serializer_class = MatchSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['season', ]
    http_method_names = ['get', 'head']

    def get_queryset(self):
        season = self.request.query_params['season']

        if season:
            query = Matches.objects.raw('''SELECT 1 as id ,winner, COUNT(*) 
                                              FROM matches WHERE season=%s
                                              GROUP BY winner 
                                              ORDER BY COUNT(*) DESC 
                                              LIMIT 4;''', [season])

            return query


class TossAPI(ModelViewSet):
    """ Team winning the most number of tosses """
    serializer_class = TossSerializer
    http_method_names = ['get', 'head']

    def get_queryset(self):
        season = self.request.query_params['season']
        print(season)
        if season:
            query = Matches.objects.raw('''SELECT 1 as id ,toss_winner, COUNT(toss_winner) 
                                               FROM matches WHERE season=%s
                                               GROUP BY toss_winner 
                                               ORDER BY COUNT(toss_winner) DESC 
                                               ''', [season])

            return query


class YearsAPI(ModelViewSet):
    """ Season api """
    queryset = Matches.objects.order_by('season').values('season').distinct()
    serializer_class = YearSerializer


class PlayerOfMatchAPI(ModelViewSet):
    """ Player won maximum  number of Player of the Match award"""
    serializer_class = PlayerOfMatchSerializer
    http_method_names = ['get', 'head']

    def get_queryset(self):
        season = self.request.query_params['season']
        print(season)
        if season:
            query = Matches.objects.raw('''SELECT 1 as id ,player_of_match, COUNT(*) 
                                               FROM matches WHERE season=%s
                                               GROUP BY player_of_match 
                                               ORDER BY COUNT(*) DESC 
                                               ''', [season])

            return query


class MaxMatchAPI(ModelViewSet):
    """ Team won max match in a season """
    serializer_class = MaxMatchSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['season', ]
    http_method_names = ['get', 'head']

    def get_queryset(self):
        season = self.request.query_params['season']

        if season:
            query = Matches.objects.raw('''SELECT 1 as id ,winner, COUNT(*) 
                                              FROM matches WHERE season=%s
                                              GROUP BY winner 
                                              ORDER BY COUNT(*) DESC 
                                              ''', [season])

            return query


class LocationAPI(ModelViewSet):
    """ Which Location won most wins """
    serializer_class = LocationSerializer

    def get_queryset(self):
        season = self.request.query_params['season']

        if season:
            query = Matches.objects.raw('''SELECT 1 as id, venue ,count(venue) from matches where winner = 
                                        (select winner from matches where season=%s 
                                        group by winner order by count(winner) DESC
                                        LIMIT 1) and season = '2017'
                                        GROUP BY venue order by count(venue) DESC;''', [season])

            return query


class HighestMarginRunAPI(ModelViewSet):
    """ Team won by highest margin of runs in season"""
    serializer_class = HighestMarginRunSerializer

    def get_queryset(self):
        season = self.request.query_params['season']
        print(season)
        if season:
            query = Matches.objects.raw('''SELECT 1 as id, winner from matches where win_by_runs=(select max(
            win_by_runs) from matches where season=%s);''',[season])

            return query


class HighestMarginWicketsAPI(ModelViewSet):
    """ Team won with highest number of wickets """
    serializer_class = HighestMarginWicketsSerializer

    def get_queryset(self):
        season = self.request.query_params['season']
        print(season)
        if season:
            query = Matches.objects.raw('''SELECT 1 as id, winner from matches where win_by_wickets=(select max(
            win_by_wickets)from matches where season=%s) and season=%s;''',[season,season])

            return query


class TossWinnerAPI(ModelViewSet):
    """ Team won the toss and the match """
    serializer_class = TossWinnerSerializer

    def get_queryset(self):
        season = self.request.query_params['season']
        print(season)
        if season:
            query = Matches.objects.raw('''SELECT 1 as id, COUNT(*) FROM matches where toss_winner=winner and 
            season=%s;''', [season])

            return query
