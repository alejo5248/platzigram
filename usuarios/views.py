from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models	import User
from usuarios.models import Perfil
from django.db.utils import IntegrityError
from usuarios.forms import ProfileForm

# Create your views here.

def update_profile(request):
	perfil= request.user.perfil

	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES)
		if form.is_valid():

			data = form.cleaned_data

			perfil.website=data['website']
			perfil.telefono=data['telefono']
			perfil.biografia=data['biografia']
			perfil.imagen=data['imagen']
			perfil.save()

			return redirect ('update_profile')
	else:
		form = ProfileForm()

	return render(request =request,template_name= 'usuarios/update_profile.html', context={'perfil':perfil, 'user':request.user, 'form':form})

def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user:
			login(request, user)
			return redirect('post')
		else:
			return render(request, 'usuarios/login.html', {'error': 'invalid username and password'})


	return render(request, 'usuarios/login.html')



def signup_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		password_confirmation = request.POST['password_confirmation']


		if password != password_confirmation:
			return render(request, 'usuarios/signup.html', {'error' : 'password incorrecto'})
		try :
			user = User.objects.create_user(username=username, password=password)
		except IntegrityError:
			return render(request, 'usuarios/signup.html', {'error' : 'el usuario ya existe'})

		
		
		user.nombre = request.POST['nombre']
		user.apellido = request.POST['apellido']
		user.email = request.POST['email']
		user.save()

		perfil = Perfil(user=user)
		perfil.save()
		return redirect('login')




	return render(request, 'usuarios/signup.html')


@login_required
def logout_view ( request ):
    logout ( request )
    return redirect ('login')	