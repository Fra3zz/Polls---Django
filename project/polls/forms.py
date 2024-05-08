from django import forms

class pollForm(forms.Form):
    Question = forms.CharField(max_length=200, label="What's your polling question?")
    answere = forms.CharField(max_length=200, label="Input your answer")