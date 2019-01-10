from django import forms
from django.contrib.auth.models	import User
from usuarios.models import Perfil


class SignupForm(forms.Form):
	username = forms.CharField(min_length=4, max_length=60)
	password = forms.CharField(max_length=70, widget=forms.PasswordInput())
	password_confirmation = forms.CharField(max_length=70, widget=forms.PasswordInput())
	first_name = forms.CharField(min_length=2, max_length=50)
	last_name = forms.CharField(min_length=2, max_length=50)
	email = forms.CharField(min_length=7, max_length=100, widget=forms.EmailInput())

	def clean_username(self):

		username = self.cleaned_data['username']
		username_taken = User.objects.filter(username=username).exists()
		if username_taken:
			raise forms.ValidationError('El nombre de usuario ya está en uso.')
		return username

	def clean(self):
		data = super().clean()

		password = data['password']
		password_confirmation = data['password_confirmation']

		if password != password_confirmation:
			raise forms.ValidationError('el password no coincide.')
		return data

	def save(self):
		data = self.cleaned_data
		data.pop('password_confirmation')

		user= User.objects.create_user(**data)
		perfil = Perfil(user=user)
		perfil.save()






