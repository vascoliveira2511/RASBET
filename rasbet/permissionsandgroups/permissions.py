from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType

from models.game import Game
from models.outcome import Outcome
from models.wallet import Wallet

content_games = ContentType.objects.get_for_model(Game)
content_outcomes = ContentType.objects.get_for_model(Outcome)
content_wallet = ContentType.objects.get_for_model(Wallet)

permission = Permission.objects.create(
   codename='mod_games',
   name='Can Moderate Games',
   content_type=content_games,
)


permission = Permission.objects.create(
   codename ='can_bet_game',
   name ='Can bet on games',
   content_type = content_games
)

permission = Permission.objects.create(
   codename ='can_mod_outcomes',
   name ='Can moderate outcomes',
   content_type = content_outcomes
)

permission = Permission.objects.create(
   codename ='can_view_open_games',
   name ='Can View Open Games',
   content_type = content_games
)

permission = Permission.objects.create(
   codename ='can_view_games_without_odds',
   name ='Can View Games Without Odds',
   content_type = content_games
)

permission = Permission.objects.create(
   codename ='can_view_closed_games',
   name ='Can View Closed Games',
   content_type = content_games
)

permission = Permission.objects.create(
   codename ='can_view_wallet',
   name ='Can View Wallet',
   content_type = content_wallet
)


admin_group, created = Group.objects.get_or_create(name='Admin')
admin_group.permissions.set('can_mod_game', 'can_view_closed_games', 'can_view_open_games')

specialist_group, created = Group.objects.get_or_create(name='Specialist')
specialist_group.permissions.set('can_mod_outcomes', 'can_view_games_without_odds')


bet_user_group, created = Group.objects.get_or_create(name='Bet_User')
bet_user_group.permissions.set('can_bet_game', 'can_view_open_games', 'can_view_wallet')