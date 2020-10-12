from rest_framework.serializers import ModelSerializer
from .models import Matches, Delivery
from rest_framework import serializers


class MatchSerializer(ModelSerializer):
    count = serializers.IntegerField(required=True)
    winner = serializers.CharField(max_length=255)

    class Meta:
        model = Matches
        fields = ('winner', 'count')


class TossSerializer(ModelSerializer):
    count = serializers.IntegerField(required=True)
    toss_winner = serializers.CharField(max_length=255)
    season = serializers.CharField(max_length=50)

    class Meta:
        model = Matches
        fields = ('season', 'toss_winner', 'count')


class PlayerOfMatchSerializer(ModelSerializer):
    count = serializers.IntegerField(required=True)
    player_of_match = serializers.CharField(max_length=255)

    class Meta:
        model = Matches
        fields = ('player_of_match', 'count')


class YearSerializer(ModelSerializer):
    class Meta:
        model = Matches
        fields = ('season',)


class MaxMatchSerializer(ModelSerializer):
    count = serializers.IntegerField(required=True)
    winner = serializers.CharField(max_length=255)


    class Meta:
        model = Matches
        fields = ('winner', 'count')


class LocationSerializer(ModelSerializer):
    count = serializers.IntegerField(required=True)

    class Meta:
        model = Matches
        fields = ('count', 'venue',)


class HighestMarginRunSerializer(ModelSerializer):
    class Meta:
        model = Matches
        fields = ('winner',)


class HighestMarginWicketsSerializer(ModelSerializer):
    class Meta:
        model = Matches
        fields = ('winner',)


class TossWinnerSerializer(ModelSerializer):
    count = serializers.IntegerField(required=True)

    class Meta:
        model = Matches
        fields = ('count',)
