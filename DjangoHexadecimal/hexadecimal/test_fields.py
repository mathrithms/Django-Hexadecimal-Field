from django import forms
from django.forms import fields_for_model
from django.db import models
from django.test import TestCase

from .fields import HexadecimalField


class HexaModel(models.Model):
    hexa = HexadecimalField(format='0x')

    class Meta:
        app_label = 'hexadecimal'

class HexadecimalFieldTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_model_formfield_doesnt_raise(self):
        try:
            fields_for_model(HexaModel())
        except AttributeError:
            self.fail('Raised Attribute Error')

