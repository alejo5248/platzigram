from django.urls import path
from posts import views


urlpatterns =[


	path('', views.PostsFeedView.as_view(), name='post'),
    path('new/',views.CreatePostView.as_view(), name='create_post'),
    path(route='posts/<int:pk>/', view=views.PostDetailView.as_view(), name='detalle')

]