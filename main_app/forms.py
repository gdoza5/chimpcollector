from django.forms import ModelForm
from .models import Shift

class ShiftForm(ModelForm):
    class Meta:
        model = Shift
        fields = ['date','shiftSeg']