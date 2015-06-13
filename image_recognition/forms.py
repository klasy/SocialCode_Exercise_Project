# -*- coding: utf-8 -*-
from django import (forms, VERSION)
from models import UploadModel

class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadModel
        if VERSION >= (1, 6):
            fields = '__all__'  # eliminate RemovedInDjango18Warning
