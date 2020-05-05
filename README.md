# cloudwatch-weather

This application creates a CloudWatch dashboard for the monitoring
of the weather in Dublin.


## Arch

In a nutshell, the app uses a CloudWatch trigger, that every
30 minutes invoke a lambda function.
The lambda function collects weather metrics from met.ie, and
pushes these metrics back to CloudWatch.

The CloudFormation template provided also includes a CloudWatch dashboard
displaying:
1. Temperature
2. Rainfall
3. Pressure
4. Humidity
5. WindSpeed

You could then add alarms if you want to be notified if certain weather conditions
are recorded (e.g. send a email if wind are above a certain threshold)

Below are a resource diagram created by the CF/SAM template: 
```
                             ┌──────────────────┐                              
                             │      met.ie      │                              
                             └─────────▲────────┘                              
                                       │                                       
                                       │                                       
                                       │                                       
┌─────────────────────┐      ┌──────────────────┐       ┌─────────────────────┐
│                     │      │                  │       │                     │
│  CloudWatch Event   ├──────▶      Lambda      ├───────▶     CloudWatch      │
│   (every 30 mins)   │      │                  │       │       Metrics       │
│                     │      │                  │       │                     │
└─────────────────────┘      └──────────────────┘       └──────────▲──────────┘
                                                                   │           
                                                                   │           
                                                                   │           
                                                        ┌──────────┴──────────┐
                                                        │                     │
                                                        │     CloudWatch      │
                                                        │      Dashboard      │
                                                        │                     │
                                                        └─────────────────────┘
```

## Dashboard

![screenshot](https://github.com/donedeal-giorgio/cloudwatch-weather/raw/master/docs/dublin_weather.png "Dashboard")

## Development
Create a python3 virtual env with:

```bash
git clone git@github.com:donedeal-giorgio/cloudwatch-weather.git cloudwatch-weather
cd cloudwatch-weather
python3 -m venv .venv
source .venv/bin/activate
pip install -r requiremnts.txt
pip install -e .
pytest -s
```

## Deployment

This application uses AWS Serverless Application Model (SAM)[https://aws.amazon.com/serverless/sam/]
to deploy a stack containing the following resources:
1. Lambda function getting metEirann weather data for today
2. An AWS CloudWatch event that triggers the lambda on a 30 mins schedule.
3. The definition of the cloudwatch dashboard [todo]

To deploy this application in your own stack, first follow the development steps.
The issue the following commands:

```bash
cd aws-weather
sam build --guided
sam deploy
```


