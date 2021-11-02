from django import forms


class TestForm(forms.Form):
    keyword = forms.CharField(label='keyword', max_length=50)
