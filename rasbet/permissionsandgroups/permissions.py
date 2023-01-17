from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType

from models.game import Game
from models.outcome import Outcome
from models.wallet import Wallet
from models.bet import Bet
from models.event import Event
from models.user import User

content_games = ContentType.objects.get_for_model(Game)
content_outcomes = ContentType.objects.get_for_model(Outcome)
content_wallet = ContentType.objects.get_for_model(Wallet)
content_bets = ContentType.objects.get_for_model(Bet)
content_events = ContentType.objects.get_for_model(Event)
content_users = ContentType.objects.get_for_model(User)


permission = Permission.objects.create(
    codename='can_view_closed_bets',
    name='Can View Closed Bets',
    content_type=content_bets
)

permission = Permission.objects.create(
    codename='can_view_open_bets',
    name='Can View Open Bets',
    content_type=content_bets
)

permission = Permission.objects.create(
    codename='can_view_suspended_bets',
    name='Can View Suspended Bets',
    Content_type=content_bets
)

permission = Permission.objects.create(
    codename='can_view_bets_without_outcome',
    name='Can View Bets Without Outcome',
    Content_type=content_bets
)

permission = Permission.objects.create(
    codename='can_mod_outcomes',
    name='Can moderate outcomes',
    content_type=content_outcomes
)
permission = Permission.objects.create(
    codename='mod_games',
    name='Can Moderate Games',
    content_type=content_games,
)

permission = Permission.objects.create(
    codename='can_view_games',
    name='Can View Games',
    content_type=content_games
)

permission = Permission.objects.create(
    codename='can_view_wallet',
    name='Can View Wallet',
    content_type=content_wallet
)

permission = Permission.objects.create(
    codename='can_mod_wallet',
    name='Can Modify Wallet',
    content_type=content_wallet
)

permission = Permission.objects.create(
    codename='can_view_events',
    name='Can View Events',
    content_type=content_events
)

permission = Permission.objects.create(
    codename='can_mod_events',
    name='Can Modify Events',
    Content_type=content_events
)

permission = Permission.objects.create(
    codename='can_edit_profile',
    name='Can Edit Profile',
    Content_type=content_users
)

permission = Permission.objects.create(
    codename='can_reset_password',
    name='Can Reset Password',
    content_type=content_users
)

admin_group, created = Group.objects.get_or_create(name='Admin')
admin_group.permissions.set('can_reset_password',
                            'can_view_closed_bets', 'can_view_open_bets', 'can_view_suspended_bets', 'can_view_bets_without_outcome',
                            'can_mod_events', 'can_view_events')

specialist_group, created = Group.objects.get_or_create(name='Specialist')
specialist_group.permissions.set('can_reset_password',
                                 'can_mod_game', 'can_mod_outcomes', 'can_view_suspended_bets', 'can_view_bets_without_outcome')


bet_user_group, created = Group.objects.get_or_create(name='Bet_User')
bet_user_group.permissions.set('can_edit_profile', 'can_reset_password'
                               'can_bet_game', 'can_view_open_games', 'can_view_wallet', 'can_mod_wallet')
