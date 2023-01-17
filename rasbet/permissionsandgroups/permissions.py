from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

content_type = ContentType.objects.get_for_model(game)

permission = Permission.objects.create(
   codename='mod_games',
   name='Can Moderate Games',
   content_type=content_type,
)