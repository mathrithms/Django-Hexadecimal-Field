import re
import django
from django.core.validators import RegexValidator
from django.db import models
if django.VERSION >= (2, 0):
    from django.utils.translation import gettext_lazy as _
else:
    from django.utils.translation import ugettext_lazy as _

HEXA_RE_0x= re.compile('^0[xX][0-9a-fA-F]+$')
HEXA_0x_VALIDATOR= RegexValidator(HEXA_RE_0x, _('Enter a valid hex number '),'invalid')
#0x format

HEXA_RE_hash= re.compile('^#[A-Fa-f0-9]+$')
HEXA_hash_VALIDATOR= RegexValidator(HEXA_RE_hash, _('Enter a valid hex number '),'invalid')
## format

HEXA_RE_h= re.compile('^[A-Fa-f0-9]+[hH]$')
HEXA_h_VALIDATOR= RegexValidator(HEXA_RE_h, _('Enter a valid hex number '),'invalid')
#h format

HEXA_RE_normal= re.compile('^[A-Fa-f0-9]+$')
HEXA_normal_VALIDATOR= RegexValidator(HEXA_RE_normal, _('Enter a valid hex number '),'invalid')
#normal format

VALIDATORS_PER_FORMAT = {
    '0x': HEXA_0x_VALIDATOR,
    'hash': HEXA_hash_VALIDATOR,
    'h': HEXA_h_VALIDATOR,
    'normal': HEXA_normal_VALIDATOR
}

DEFAULT_PER_FORMAT = {
    '0x': '0xFFFFFF',
    'hash': '#FFFFFF',
    'h': 'FFFFFFh',
    'normal': 'FFFFFF'
}

class HexadecimalField(models.CharField):
    validator_required = []
    def __init__(self,*args,**kwargs):
        self.format = kwargs.pop('format', '0x').lower()
        if self.format not in ['0x', 'hash','h','normal']:
            raise ValueError('Unsupported format: {}'.format(self.format))
        self.default_validators = [VALIDATORS_PER_FORMAT[self.format]] #validator according to format

        if kwargs.get('null'):
            kwargs.setdefault('blank', True)
            kwargs.setdefault('default', None)
        elif kwargs.get('blank'):
            kwargs.setdefault('default', '')
        else:
            kwargs.setdefault('default', DEFAULT_PER_FORMAT[self.format]) #stores sample format
        #check args 

        super(HexadecimalField, self).__init__(*args, **kwargs)


