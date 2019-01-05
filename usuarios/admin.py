from django.contrib import admin
from usuarios.models import Perfil
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):

	list_display =('pk','user','telefono','website','imagen')
	list_display_links=('pk','user','telefono')
	search_fields=('user__email','user__nombre','user__apellido','telefono')
	list_filter=('creado','modificado')

	fieldsets=(
		('Perfil', {
			'fields':('user','imagen'),
					

			}),
		('informacion_extra',{

			'fields':('website','telefono'),

			}),
		('metadatos',{

			'fields':('creado','modificado'),

			}),

		)

	readonly_fields=('creado','modificado')
	
class PerfilEnlinea(admin.StackedInline):

	model = Perfil
	can_delete = False
	verbose_name_plural = 'perfiles'

class UserAdmin(BaseUserAdmin):

	inlines = (PerfilEnlinea,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
