from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

# Forms
from posts.forms import PostForm

# Models
from posts.models import Post
# Create your views here.


class PostsFeedView(LoginRequiredMixin, ListView):

	template_name = 'posts/feed.html'
	model= Post
	orderign = ('-creado',)
	paginate_by = 2
	context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):

	template_name = 'posts/detalle.html'
	queryset = Post.objects.all()
	context_object_name = 'post'


class CreatePostView(LoginRequiredMixin, CreateView):

	template_name='posts/new.html'
	form_class=PostForm
	success_url=reverse_lazy('posts:post')

	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		context['user']=self.request.user
		context['perfil']=self.request.user.perfil
		return context
