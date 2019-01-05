
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

	user=models.ForeignKey(User, on_delete=models.CASCADE)
	perfil=models.ForeignKey('usuarios.Perfil', on_delete=models.CASCADE)
	titulo=models.CharField(max_length=50)
	foto=models.ImageField(upload_to='posts/images')
	creado=models.DateTimeField(auto_now_add=True)
	modificado=models.DateTimeField(auto_now=True)

	def __str__(self):
		return'{} by @{}'.format(self.titulo, self.user.username)