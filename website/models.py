# -*- coding: utf-8 -*-
'''Consolidates all necessary models from the framework and website packages.
'''

from framework.guid.model import Guid
from framework.auth.model import User
from framework.sessions.model import Session

from website.project.model import (ApiKey, Node, NodeLog, NodeFile, NodeWikiPage,
                                   Tag, WatchConfig, MetaData, MetaSchema, Pointer)

# All models
MODELS = (User, ApiKey, Node, NodeLog, NodeFile, NodeWikiPage,
          Tag, WatchConfig, Session, Guid, MetaData, MetaSchema, Pointer)

GUID_MODELS = (User, Node, NodeFile, NodeWikiPage, Tag, MetaData)
