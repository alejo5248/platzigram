from django import forms
from posts.models import Post



class PostForm(forms.ModelForm):
	"""docstring for PostForm"""
	class Meta:

		model = Post
		fields = ('user', 'perfil','titulo', 'foto' )
