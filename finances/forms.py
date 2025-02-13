from django import forms
from finances.models import Expense, Category

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title','describe', 'value','date','categoryfk','status_choice']

        
    categoryfk = forms.ModelChoiceField(queryset=Category.objects.all(),required=True)


    