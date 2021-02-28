# Django-Hexadecimal-Field
Hexadecimal field in Django for hexadecimal inputs

## Installation

## Usage
Import the HexadecimalField from fields.py 

```python

from hexadecimal.fields import HexadecimalField
from django.db import models

class SampleModel(model.Model):
    color = HexadecimalField(max_length='25',format='hexa')

```
Note that user must specify max_length
