from django.contrib import admin

# Register your models here.
from posts.models import Post 

class PostAdmin(admin.ModelAdmin):
	list_display = ('id','user','titulo','foto')
	search_fields =('title', 'user_username', 'user_email')
	list_filter = ('creado', 'modificado')
