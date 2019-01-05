from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Perfil(models.Model):
	user = models.OneToOneField(User, on_delete= models.CASCADE )
	website=models.URLField(max_length=200, blank=True)
	telefono=models.IntegerField()
	imagen=models.ImageField(upload_to='usuarios/images',blank=True, null=True)
	creado=models.DateTimeField(auto_now_add=True)
	modificado=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.user.username


