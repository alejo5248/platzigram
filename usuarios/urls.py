from django.urls import path
from usuarios import views



urlpatterns =[
	
	


	path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('yo/perfil', views.UpdateProfileView.as_view(), name='update'),
    path(route='<str:username>/', view=views.UserDetailView.as_view(), name='detalle'),

]