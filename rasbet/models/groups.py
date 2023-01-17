from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
 
# import User model
from models.game import Game
from models.outcome import Outcome

# Code to add permission to group
content_games = ContentType.objects.get_for_model(Game)
content_goutcome = ContentType.objects.get_for_model(Outcome)

# If I want to add 'Can go Haridwar' permission to level0 ?
permission = Permission.objects.create(codename ='can_mod_game',
                                        name ='Can moderate games',
                                        content_type = content_games)

admin_group, created = Group.objects.get_or_create(name='Admin')
admin_group.permissions.set('can_mod_game')

specialist_group, created = Group.objects.get_or_create(name='Specialist')
specialist_group.permissions.add()


bet_user_group, created = Group.objects.get_or_create(name='Bet_User')
bet_user_group.permissions.set()