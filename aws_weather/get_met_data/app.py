import json
import requests
from os import getenv
from aws_embedded_metrics import metric_scope

met_metrics = [
    {
        "name": "temperature",
        "alias": "Temperature"

    },
    {
        "name": "windSpeed",
        "alias": "WindSpeed"

    },
    {
        "name": "humidity",
        "alias": "Humidity"

    },
    {
        "name": "rainfall",
        "alias": "Rainfall"
    },
    {
        "name": "pressure",
        "alias": "Pressure"
    }
]

locations = {
    "DublinSouth": "https://prodapi.metweb.ie/weather/short/South%20Dublin",
    "Dublin": "https://prodapi.metweb.ie/weather/short/Dublin",
    "DublinCity": "https://prodapi.metweb.ie/weather/short/Dublin+City",
    "DunLaoghaire": "https://prodapi.metweb.ie/weather/short/Dun%20Laoghaire"
}

LOCATION = getenv('LOCATION', 'DublinSouth')


@metric_scope
def lambda_handler(event, context, metrics):
    """Sample pure Lambda function
    """

    try:
        page = requests.get(locations[LOCATION])
        met_info = page.json()
    except requests.RequestException as e:
        print(e)
        raise e

    for met_metric in met_metrics:
        current_metric = float(met_info[met_metric['name']])
        metrics.put_metric(key=met_metric['alias'], value=current_metric, unit=None)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "OK"
        }),
    }
