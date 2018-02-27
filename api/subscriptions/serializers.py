from rest_framework import serializers as ser

from api.base.serializers import (JSONAPISerializer, IDField)

from osf.models import PreprintProvider

class FrequencyField(ser.Field):
    def to_representation(self, obj):
        pass

    def to_internal_value(self, data):
        pass

class UserProviderSubscriptionSerializer(JSONAPISerializer):
    id = IDField(source='_id', read_only=True)
    event_name = ser.CharField(read_only=True)

    class Meta:
        type_ = 'user-provider-subscription'