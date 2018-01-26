import logging
import os

from django.db import migrations
from django.contrib.auth.models import Group

from osf.models import PreprintProvider

logger = logging.getLogger(__file__)

def rename_permission_groups(*args):
    GROUP_FORMAT = 'reviews_{provider_id}_{group}'
    for provider in PreprintProvider.objects.all():
        admin_group_name = GROUP_FORMAT.format(provider_id=provider._id, group='admin')
        moderator_group_name = GROUP_FORMAT.format(provider_id=provider._id, group='moderator')

        try:
            admin_group = Group.objects.get(name=admin_group_name)
        except Group.DoesNotExist:
            admin_group = None

        try:
            moderator_group = Group.objects.get(name=moderator_group_name)
        except Group.DoesNotExist:
            moderator_group = None

        if admin_group:
            admin_group.name = GROUP_FORMAT.format(provider_id=provider.id, group='admin')
            admin_group.save()
        if moderator_group:
            moderator_group.name = GROUP_FORMAT.format(provider_id=provider.id, group='moderator')
            moderator_group.save()

def revert(*args):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('osf', '0076_action_rename'),
    ]

    operations = [
        migrations.RunPython(rename_permission_groups, revert),
    ]
