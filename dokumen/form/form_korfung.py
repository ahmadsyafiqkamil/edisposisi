#  Copyright (c) 2019.
#  Ahmad Syafiq Kamil
from builtins import print

from django import forms
from ..models import ValidasiDokumen
from django.conf import settings
from django.forms import ModelMultipleChoiceField

from ..models import Dokumen, Fungsi
from bootstrap_datepicker_plus import DatePickerInput, DateTimePickerInput, MonthPickerInput
from django_select2.forms import Select2MultipleWidget
from dokumen.models import Klasifikasi, Fungsi, Dokumen, JenisDokumen
from accounts.models import User
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _

# class TTDForm(forms.ModelForm):
#
#     class Meta:
#         model = ValidasiDokumen
#         fields = ('')