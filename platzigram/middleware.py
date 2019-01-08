from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:

	def __init__(self, get_response):

	
		self.get_response = get_response

	def __call__(self, request):

		if not request.user.is_anonymous:
			perfil = request.user.perfil
			if not perfil.imagen or not perfil.biografia :
				if request.path not in [reverse('update_profile'), reverse ('logout')]:
					return redirect ('update_profile')

		response = self.get_response(request)
		return response 