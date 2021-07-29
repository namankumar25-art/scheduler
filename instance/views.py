from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
import boto3
from boto_driver import (instance_schedule_create_driver, 
						instance_schedule_update_driver, 
						instance_schedule_fetch_driver,
						instance_schedule_delete_driver)

@api_view(['GET'])
def instanceoverview(request):

	api_urls={

		'read_schedule':'schedule/fetch/',
		'create_schedule':'schedule/create/',
		'update_schedule':'schedule/update/',
		'delete_schedule':'schedule/delete/',
	}

	return Response(api_urls)

@api_view(['GET'])
def instance_schedule_fetch(request):

	a = request.GET.dict()

	response={}

	context={

			'instance_id':a['instance_id'],
			'action':'start'				

	}
	response['start_schedule'] = instance_schedule_fetch_driver(context)
	response['start_schedule'].pop('ResponseMetadata')

	context={

			'instance_id':a['instance_id'],
			'action':'stop'				

	}

	response['stop_schedule'] = instance_schedule_fetch_driver(context)	
	response['stop_schedule'].pop('ResponseMetadata')

	return Response({'schedule':response})

@api_view(['POST'])
def instance_schedule_create(request):

	a = json.loads(request.body)	

	context={

			'instance_id':a['instance_id'],
			'action':'start',
			'frequency':a['config']['start_schedule']				

	}
	instance_schedule_create_driver(context)

	context={

			'instance_id':a['instance_id'],
			'action':'stop',
			'frequency':a['config']['stop_schedule']				

	}
	instance_schedule_create_driver(context)


	return Response({"msg":"schedule created"})


@api_view(['PATCH'])
def instance_schedule_update(request):

	a = json.loads(request.body)	

	context={

			'instance_id':a['instance_id'],
			'action':'start',
			'frequency':a['config']['start_schedule']				

	}
	instance_schedule_update_driver(context)

	context={

			'instance_id':a['instance_id'],
			'action':'stop',
			'frequency':a['config']['stop_schedule']				

	}
	instance_schedule_update_driver(context)


	return Response({"msg":"schedule updated"})


@api_view(['PATCH'])
def instance_schedule_delete(request):

	a = json.loads(request.body)	

	context={

			'instance_id':a['instance_id'],
			'action':'start',	

	}
	instance_schedule_delete_driver(context)

	context={

			'instance_id':a['instance_id'],
			'action':'stop',			

	}
	instance_schedule_delete_driver(context)


	return Response({"msg":"schedule deleted"})