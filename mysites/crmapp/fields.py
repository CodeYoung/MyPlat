import string

from django import forms
from django.core.validators import validate_email
from django.forms.widgets import CheckboxInput
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _

#from .conf import settings

class HoneyPotField(forms.BooleanField):
    widget = CheckboxInput

    def __init__(self, *args, **kwargs):
        super(HoneyPotField, self).__init__(*args, **kwargs)
        self.required = False
        if not self.label:
            self.label = _('Are you human? (Sorry, we have to ask!)')
        if not self.help_text:
            self.help_text = _('Please don\'t check this box if you are a human.')

    def validate(self, value):
        if value:
            raise forms.ValidationError(_('Doh! You are a robot!'))