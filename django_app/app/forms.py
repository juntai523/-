from django import forms
from .models import Memo

class PostForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ['content']
        widgets = {
            'content': forms.Textarea
        }

CHOICE_FIELD_RECODE_NUMBERS = (
    ('10', '10件'),
    ('15', '15件'),
    ('30', '30件'),
)

class RecordNumberForm(forms.Form):
    record_number = forms.ChoiceField(
        widget=forms.Select(attrs={'onchange': 'submit(this.form)'}), 
        choices=CHOICE_FIELD_RECODE_NUMBERS
    )
CHOICE_FIELD_RECODE_ORDERS = (
    ('reverse', '新着順'),
    ('', '古い順'),
)
class RecordOrderForm(forms.Form):
    record_order = forms.ChoiceField(
        widget=forms.Select(attrs={'onchange': 'submit(this.form)'}), 
        choices=CHOICE_FIELD_RECODE_ORDERS
    )
#class MemoForm(forms.Form):
#    content=forms.Charfield

