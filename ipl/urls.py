from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .api import MatchAPI, TossAPI, YearsAPI, PlayerOfMatchAPI, MaxMatchAPI, LocationAPI, HighestMarginRunAPI, \
    HighestMarginWicketsAPI, TossWinnerAPI
from . import views

router = DefaultRouter()

router.register('match',
                MatchAPI,
                basename='match')

router.register('toss',
                TossAPI,
                basename='toss')

router.register('year',
                YearsAPI,
                basename='year')

router.register('player-match-api',
                PlayerOfMatchAPI,
                basename='player-match')

router.register('max-match-api',
                MaxMatchAPI,
                basename='player-match')

router.register('location-api',
                LocationAPI,
                basename='player-match')

router.register('highest-margin-api',
                HighestMarginRunAPI,
                basename='player-match')

router.register('highest-wicket-api',
                HighestMarginWicketsAPI,
                basename='player-match')

router.register('toss-winner',
                TossWinnerAPI,
                basename='player-match')

urlpatterns = [
    url('bating-api/',
        views.get_batting,
        name='match'),

    url('get-venue-api',
        views.get_most_matches),


]
urlpatterns += router.urls
