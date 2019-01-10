
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, FormView, UpdateView
from django.urls import reverse, reverse_lazy
from usuarios.forms import  SignupForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models import Post
from usuarios.models import Perfil
from django.contrib.auth import views as auth_views

# Create your views here.


class UserDetailView(LoginRequiredMixin, DetailView):

	template_name = 'usuarios/detalle.html'
	slug_field = 'username'
	slug_url_kwarg = 'username'
	queryset = User.objects.all()
	context_object_name = 'user'

	def get_context_data(self, **kwargs):

		context = super().get_context_data(**kwargs)
		user = self.get_object()
		context['posts'] = Post.objects.filter(user=user).order_by('-creado')
		return context

class SignupView(FormView):
	template_name='usuarios/signup.html'
	form_class=SignupForm
	success_url=reverse_lazy('usuarios:login')

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)

class UpdateProfileView(LoginRequiredMixin, UpdateView):
	template_name='usuarios/update_profile.html'
	model = Perfil
	fields=['website','biografia','telefono', 'imagen']

	def get_object(self):
		return self.request.user.perfil 

	def get_success_url(self):

		username=self.object.user.username
		return reverse('usuarios:detalle', kwargs={'username':username})
	



def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user:
			login(request, user)
			return redirect('posts:post')
		else:
			return render(request, 'usuarios/login.html', {'error': 'invalid username and password'})


	return render(request, 'usuarios/login.html')




@login_required
def logout_view ( request ):
    logout ( request )
    return redirect ('usuarios:login')	