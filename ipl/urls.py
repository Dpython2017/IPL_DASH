from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .api import MatchAPI, TossAPI, YearsAPI, PlayerOfMatchAPI, MaxMatchAPI, LocationAPI, HighestMarginRunAPI, \
    HighestMarginWicketsAPI, TossWinnerAPI
from . import views
from rest_framework import permissions

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
                basename='max-match')

router.register('location-api',
                LocationAPI,
                basename='location')

router.register('highest-margin-api',
                HighestMarginRunAPI,
                basename='highest-margin')

router.register('highest-wicket-api',
                HighestMarginWicketsAPI,
                basename='highest-wicket')

router.register('toss-winner',
                TossWinnerAPI,
                basename='toss-winner')

urlpatterns = [
    url('bating-api/',
        views.get_batting,
        name='match'),

    url('get-venue-api',
        views.get_most_matches),

]
urlpatterns += router.urls
