from django import forms
from .models import Tag
from .widgets import CustomCheckboxSelectMultiple


class SampleForm(forms.Form):
    tags = forms.ModelMultipleChoiceField(
        label='タグ', queryset=Tag.objects, required=False,
        widget=CustomCheckboxSelectMultiple,
    )
    a = forms.MultipleChoiceField

