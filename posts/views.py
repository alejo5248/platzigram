from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

posts = [
	{

		'title' : 'guitarra',
		'user' :{
			'name': 'Alejandro Hurtado',
			'picture' : 'https://picsum.photos/60/60/?image=1027'

		},
		'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'photo' : 'https://picsum.photos/800/600?image=1036',
	},
		{

		'title' : 'musica',
		'user' :{
			'name': 'Carolina Hincapie',
			'picture' :  'https://picsum.photos/60/60/?image=1005'

		},
		'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'photo' : 'https://picsum.photos/800/800/?image=903',
	}
]
@login_required
def list_posts(request):
	return render(request, 'posts/feed.html', {'posts':posts})