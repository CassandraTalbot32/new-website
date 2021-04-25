from django import forms

class QuoteForm(forms.Form):
    name = forms.CharField(label='Name', required=True)
    email = forms.EmailField(label='Email address', required=True)
    website = forms.URLField(label='Current website', required=False)
    number = forms.CharField(label='Contact number', required=True)
    about = forms.CharField(label='About the project', widget=forms.Textarea, required=True)
    
    
      