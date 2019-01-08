from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Forms
from posts.forms import PostForm

# Models
from posts.models import Post
# Create your views here.


@login_required
def list_posts(request):
	posts = Post.objects.all().order_by('-creado')

	return render(request=request,template_name= 'posts/feed.html',context= {'posts':posts})


@login_required
def create_posts(request):

	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('post')

	else:
		form= PostForm()

	return render(
		request=request ,
		template_name = 'posts/new.html',
		context={
			'form':form,
			'user':request.user,
			'perfil':request.user.perfil
		}
	)
