from __future__ import absolute_import

from django import forms
from django.contrib.auth.models import Group

from osf.models import AdminProfile, PreprintProvider


class LoginForm(forms.Form):
    email = forms.CharField(label=u'Email', required=True)
    password = forms.CharField(
        label=u'Password',
        widget=forms.PasswordInput(render_value=False),
        required=True
    )


class GroupPermissionModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        default_label = unicode(obj)
        if 'reviews' in default_label and 'osf' not in default_label:
            splits = default_label.split('_')
            provider_id = splits[1]
            permission_type = splits[2]
            customize_label = 'reviews {provider_name} {permission_type}'.format(
                provider_name=PreprintProvider.objects.get(id=provider_id).name,
                permission_type=permission_type
            )
            return customize_label
        else:
            return default_label


class UserRegistrationForm(forms.Form):
    """ A form that finds an existing OSF User, and grants permissions to that
    user so that they can use the admin app"""

    osf_id = forms.CharField(required=True, max_length=5, min_length=5)

    group_perms = GroupPermissionModelMultipleChoiceField(
        queryset=Group.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )


class DeskUserForm(forms.ModelForm):
    class Meta:
        model = AdminProfile
        fields = ['desk_token', 'desk_token_secret']
