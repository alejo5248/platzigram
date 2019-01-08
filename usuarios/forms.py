from django import forms

class ProfileForm(forms.Form):

	website = forms.URLField(max_length=200, required=True)
	biografia = forms.CharField(max_length=500, required=True)
	telefono= forms.IntegerField(required=False)
	imagen=forms.ImageField()
