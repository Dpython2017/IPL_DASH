from django.db import models


class TimeStamped(models.Model):
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        abstract = True


class Matches(TimeStamped):
    class TossChoice(models.TextChoices):
        field = 'field'
        bat = 'bat'

    season = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    event_date = models.DateField(null=True, blank=True)
    team_1 = models.CharField(max_length=255, null=True, blank=True)
    team_2 = models.CharField(max_length=255, null=True, blank=True)
    toss_winner = models.CharField(max_length=255, null=True, blank=True)
    toss_decision = models.CharField(max_length=255, choices=TossChoice.choices,
                                     default='field', null=True, blank=True)
    result = models.CharField(max_length=50, null=True, blank=True)
    dl_applied = models.BooleanField(default=0, null=True, blank=True)
    winner = models.CharField(max_length=255, null=True, blank=True)
    win_by_runs = models.IntegerField(null=True, blank=True)
    win_by_wickets = models.IntegerField(null=True, blank=True)
    player_of_match = models.CharField(max_length=255, null=True, blank=True)
    venue = models.CharField(max_length=255, null=True, blank=True)
    umpire_1 = models.CharField(max_length=255, null=True, blank=True)
    umpire_2 = models.CharField(max_length=255, null=True, blank=True)
    umpire_3 = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'matches'
        verbose_name_plural = 'Matches'

    def __str__(self):
        return self.toss_winner


class Delivery(TimeStamped):
    match = models.ForeignKey(Matches, on_delete=models.DO_NOTHING)
    inning = models.IntegerField(null=True, blank=True)
    batting_team = models.CharField(max_length=100, null=True, blank=True)
    bowling_team = models.CharField(max_length=100, null=True, blank=True)
    overs = models.IntegerField(null=True, blank=True)
    ball = models.IntegerField(null=True, blank=True)
    batsman = models.CharField(max_length=100, null=True, blank=True)
    non_striker = models.CharField(max_length=100, null=True, blank=True)
    bowler = models.CharField(max_length=100, null=True, blank=True)
    is_super_over = models.BooleanField(default=0, null=True, blank=True)
    wide_runs = models.IntegerField(null=True, blank=True)
    bye_runs = models.IntegerField(null=True, blank=True)
    leg_bye_run = models.IntegerField(null=True, blank=True)
    no_ball_runs = models.IntegerField(null=True, blank=True)
    penalty_runs = models.IntegerField(null=True, blank=True)
    batsman_runs = models.IntegerField(null=True, blank=True)
    extra_runs = models.IntegerField(null=True, blank=True)
    total_runs = models.IntegerField(null=True, blank=True)
    player_dismissed = models.CharField(max_length=100, null=True, blank=True)
    dismissal_kind = models.CharField(max_length=100, null=True, blank=True)
    fielder = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'delivery'
        verbose_name_plural = 'Delivery'
