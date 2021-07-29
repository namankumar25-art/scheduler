# Serverless AWS Instance Scheduler

 An API endpoint for scheduling an AWS EC2 instance using AWS Lambda. The endpoint takes JSON input from a user and can start and stop a user specified EC2 
 instance based on a schedule specified by the user.

## Description
Django based python application that exposes an API endpoint that does the following -<br/>

Creates a schedule for a specified EC2 instance using AWS Lambda.<br/>
Updates the schedule for a specified instance.<br/>
Deletes the schedule for the specified EC2 instance.<br/>
Fetches/Reads the schedule for an EC2 instance.

## Built With
```
Python, boto3
Django Rest Framework
AWS : Lambda, EC2, Cloudwatch
```

## Installation
Step 1: Clone the project files on the local machine using the following command: <br/>
```
git clone https://github.com/namankumar25-art/scheduler.git
```
Step 2: Change directory to the location of requirments.txt. Create and activate virtual environment preferably by the name of ```.env``` or ```.venv```. Install the dependencies from the requirments.txt file
```
pip install -r requirements.txt
```
Step 3: Change directory to the location of manage.py file. Run the django server using the following command:<br/>
```
python manage.py runserver
```
Step 4: Open an internet browser and go to<br/>
```
http://127.0.0.1:8000/schedule/
```

## API Endpoints <br/>

### Creating a Schedule<br/>
Navigate to http://127.0.0.1:8000/schedule/create/ <br/>
Request Payload would be as follows: <br/>
```json
{
  "instance_id": "<instance_id>",
  "config": {
    "start_schedule": "cron expression",
    "stop_schedule": "cron expression"
  }
}
``` 
This creates two individual Rules and Triggers(one each for start and stop functionality) for the schedule of specified EC2 instance. <br/>

### Updating a Schedule<br/>
Navigate to http://127.0.0.1:8000/schedule/update/ <br/>
Request Payload would be as follows: <br/>
```json
{
  "instance_id": "<instance_id>",
  "config": {
    "start_schedule": "cron expression",
    "stop_schedule": "cron expression"
  }
}
```
Request Payload is similar to "create schedule" functionality, except for the changed values of cron expressions. <br/>

### Fetching/Reading a Schedule<br/>
Navigate to http://127.0.0.1:8000/schedule/fetch/?id_instance=<instance_id> <br/>
instance_id is the identifier for the EC2 instance whose schedule is to be fetched. 

### Deleting a Schedule<br/>
Navigate to http://127.0.0.1:8000/schedule/delete/ <br/>
Request Payload would be as follows: <br/>
```json
{
    "instance_id":"<instance_id>"
}
```
This deletes the two individual Rules and Triggers(one each for start and stop functionality) for the schedule of specified EC2 instance. <br/>
