import boto3
from constants import constant

def instance_schedule_fetch_driver(context):

	events_client = boto3.client('events')

	instance_id=context['instance_id']
	action=context['action']

	name = "{0}-{1}-Trigger".format(action, instance_id)

	rule_response = events_client.describe_rule(
	    Name=name,
	)
	
	return rule_response

def instance_schedule_create_driver(context):

	lambda_client = boto3.client('lambda', aws_access_key_id=constant['aws_access_key_id'],aws_secret_access_key=constant['aws_secret_access_key'])
	events_client = boto3.client('events', aws_access_key_id=constant['aws_access_key_id'],aws_secret_access_key=constant['aws_secret_access_key'])

	instance_id=context['instance_id']
	action=context['action']
	frequency=context['frequency']			
	
	fn_name = constant['fn_name']
	fn_role = constant['fn_role']

	fn_arn = constant['fn_arn']


	name = "{0}-{1}-Trigger".format(action, instance_id)

	rule_response = events_client.put_rule(
	    Name=name,
	    ScheduleExpression=frequency,
	    State='ENABLED',
	)

	lambda_client.add_permission(
	    FunctionName=fn_name,
	    StatementId="{0}-{1}-Event".format(action, instance_id),
	    Action='lambda:InvokeFunction',
	    Principal='events.amazonaws.com',
	    SourceArn=rule_response['RuleArn'],
	)

	events_client.put_targets(
	    Rule=name,
	    Targets=[
	        {
	            'Id': "1",
	            'Arn': fn_arn,
	            'Input': '{"instance_id":"%s", "action":"%s"}'%(instance_id, action)
	        },
	    ]
	)


def instance_schedule_update_driver(context):

	lambda_client = boto3.client('lambda')
	events_client = boto3.client('events')

	instance_id=context['instance_id']
	action=context['action']
	frequency=context['frequency']		
	
	fn_name = constant['fn_name']
	fn_role = constant['fn_role']

	fn_arn = constant['fn_arn']

	name = "{0}-{1}-Trigger".format(action, instance_id)

	rule_response = events_client.put_rule(
	    Name=name,
	    ScheduleExpression=frequency,
	    State='ENABLED',
	)

	events_client.put_targets(
	    Rule=name,
	    Targets=[
	        {
	            'Id': "1",
	            'Arn': fn_arn,
	            'Input': '{"instance_id":"%s", "action":"%s"}'%(instance_id, action)
	        },
	    ]
	)


def instance_schedule_delete_driver(context):

	lambda_client = boto3.client('lambda', aws_access_key_id=constant['aws_access_key_id'],aws_secret_access_key=constant['aws_secret_access_key'])
	events_client = boto3.client('events', aws_access_key_id=constant['aws_access_key_id'],aws_secret_access_key=constant['aws_secret_access_key'])

	instance_id=context['instance_id']
	action=context['action']		
	
	fn_name = constant['fn_name']
	fn_role = constant['fn_role']

	fn_arn = constant['fn_arn']


	name = "{0}-{1}-Trigger".format(action, instance_id)

	lambda_client.remove_permission(
	    FunctionName=fn_name,
	    StatementId="{0}-{1}-Event".format(action, instance_id),
	)

	events_client.remove_targets(
	    Rule=name,
	    Ids=["1"]      	    
	)

	rule_response = events_client.delete_rule(
	    Name=name,
	)