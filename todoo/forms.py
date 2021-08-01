from django import forms


class AddTodooForm(forms.Form):
    task_name=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    status=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    user=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
