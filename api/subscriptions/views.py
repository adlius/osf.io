from rest_framework import generics

from api.base.views import JSONAPIBaseView
from api.base.utils import get_object_or_error
from osf.models import NotificationSubscription, PreprintProvider


class UserProviderSubscriptionDetail(JSONAPIBaseView, generics.RetrieveAPIView):
    view_name = 'user-provider-subscription-detail'
    view_category = 'subscriptions'

    def get_object(self):
        import ipdb
        ipdb.set_trace()
        provider_id = self.kwargs['provider_id']
        provider = PreprintProvider.objects.get(_id=provider_id)
        notification = NotificationSubscription.objects.get(provider=provider)
        return notification
