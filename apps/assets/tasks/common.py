# -*- coding: utf-8 -*-
#

from celery import shared_task

from orgs.utils import tmp_to_root_org

__all__ = ['add_nodes_assets_to_system_users']


@shared_task
@tmp_to_root_org()
def add_nodes_assets_to_system_users(nodes_keys, system_users):
    from ..models import Node
    assets = Node.get_nodes_all_assets(nodes_keys).values_list('id', flat=True)
    for system_user in system_users:
        system_user.assets.add(*tuple(assets))
