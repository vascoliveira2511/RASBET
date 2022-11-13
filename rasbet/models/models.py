from django.db import models

# Here we should type our models


class Game(models.Model):
    name = models.CharField(
        max_length=100, primary_key=True)  # name of the game used as primary key
    homeTeam = models.CharField(max_length=100)  # name of the home team
    awayTeam = models.CharField(max_length=100)  # name of the away team
    commanceTime = models.DateTimeField()  # time of the game
    completed = models.BooleanField(default=False)  # is the game completed
    # scores of the game in the format "NxN" where N is a number
    scores = models.CharField(max_length=100, default=None, null=True)

    def __str__(self):
        return self.homeTeam + " " + self.awayTeam + " " + str(self.commanceTime) + " " + str(self.completed) + " " + str(self.scores)


class User(models.Model):
    username = models.CharField(
        max_length=100, unique=True)  # username of the user
    password = models.CharField(max_length=100)  # password of the user
    email = models.CharField(
        max_length=100, default=None, null=True, unique=True)  # email of the user
    firstName = models.CharField(
        max_length=100, default=None, null=True)  # first name of the user
    lastName = models.CharField(
        max_length=100, default=None, null=True)  # last name of the user
    balance = models.FloatField(default=0.0, null=True)  # balance of the user
    # user, specialist or admin
    type = models.CharField(max_length=100, default="user")

    def __str__(self):
        return self.username + " " + self.email + " " + self.firstName + " " + self.lastName + " " + str(self.balance) + " " + self.type


class Bookmark(models.Model):
    key = models.CharField(max_length=100)  # key of the bookmark
    lastUpdate = models.DateTimeField()  # last update of the bookmark
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, verbose_name="the related game")  # game of the bookmark

    def __str__(self):
        return self.key + " " + str(self.lastUpdate) + " " + str(self.game)


class Market(models.Model):
    key = models.CharField(max_length=100)  # key of the market
    Bookmark = models.ForeignKey(
        Bookmark, on_delete=models.CASCADE, verbose_name="the related bookmark")  # bookmark of the market

    def __str__(self):
        return self.key + " " + str(self.Bookmark)


class Outcome(models.Model):
    # result of the outcome in the format name of the team or Draw
    result = models.CharField(max_length=100)
    multiplier = models.FloatField()  # multiplier of the outcome
    market = models.ForeignKey(
        Market, on_delete=models.CASCADE, verbose_name="the related market")  # the related market

    def __str__(self):
        return self.result + " " + str(self.multiplier) + " " + str(self.market)


class Bet(models.Model):

    stake = models.FloatField()  # the amount of money the user bets
    multiplier = models.FloatField()  # the multiplier of the outcome
    time = models.DateTimeField()  # the time the bet was made
    status = models.CharField(
        max_length=100, default="pending")  # pending, won or lost
    won = models.FloatField(default=0.0)  # the amount of money the user won
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="the related user")  # the user who made the bet

    def __str__(self):
        return str(self.stake) + " " + str(self.multiplier) + " " + str(self.time) + " " + self.status + " " + str(self.won) + " " + str(self.user)


class BetOutcome(models.Model):
    status = models.CharField(
        max_length=100, default="pending")  # pending, won or lost
    bet = models.ForeignKey(
        Bet, on_delete=models.CASCADE, verbose_name="the related bet")  # the bet the outcome belongs to
    outcome = models.ForeignKey(
        Outcome, on_delete=models.CASCADE, verbose_name="the related outcome")  # the outcome the bet belongs to

    def __str__(self):
        return self.status + " " + str(self.bet) + " " + str(self.outcome)
