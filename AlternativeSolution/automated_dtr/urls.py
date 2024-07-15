from django.urls import path 
from automated_dtr import views 
urlpatterns = [
	path("", views.index, name="index"),
    path('showCSV/', views.showCSV, name='showCSV'),

	]

