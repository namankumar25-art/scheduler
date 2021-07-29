from django.urls import path, include
from . import views

app_name='instance'

urlpatterns=[

	path('',views.instanceoverview, name='instance_overview'),
	path('fetch/', views.instance_schedule_fetch, name='instance-schedule-fetch'),
	path('create/', views.instance_schedule_create, name='instance-schedule-create'),
	path('update/', views.instance_schedule_update, name='instance-schedule-update'),
	path('delete/', views.instance_schedule_delete, name='instance-schedule-delete'),

]