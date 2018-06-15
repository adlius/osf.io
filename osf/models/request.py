# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from include import IncludeManager

from osf.models.base import BaseModel, ObjectIDMixin
from osf.utils.workflows import RequestTypes
from osf.models.mixins import NodeRequestableMixin, PreprintRequestableMixin


class AbstractRequest(BaseModel, ObjectIDMixin):
    class Meta:
        abstract = True

    objects = IncludeManager()

    creator = models.ForeignKey('OSFUser', related_name='submitted_%(class)s')
    comment = models.TextField(null=True, blank=True)

    @property
    def target(self):
        raise NotImplementedError()

    @property
    def request_type(self):
        raise NotImplementedError()


class NodeRequest(AbstractRequest, NodeRequestableMixin):

    target = models.ForeignKey('AbstractNode', related_name='node_requests')
    request_type = models.CharField(max_length=31, choices=RequestTypes.choices())


class PreprintRequest(AbstractRequest, PreprintRequestableMixin):

    target = models.ForeignKey('PreprintService', related_name='preprint_requests')
    request_type = models.CharField(max_length=31, choices=RequestTypes.choices())
