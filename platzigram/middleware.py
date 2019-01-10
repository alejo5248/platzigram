from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:

	def __init__(self, get_response):

	
		self.get_response = get_response

	def __call__(self, request):

		if not request.user.is_anonymous:
			perfil = request.user.perfil
			if not perfil.imagen or not perfil.biografia :
				if request.path not in [reverse('usuarios:update'), reverse ('usuarios:logout')]:
					return redirect ('usuarios:update')

		response = self.get_response(request)
		return response 