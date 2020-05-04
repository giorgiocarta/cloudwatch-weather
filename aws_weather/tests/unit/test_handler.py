import json
import mock
from unittest import TestCase

from mock import patch

# monkey patching before the decorator is loaded
patch('aws_embedded_metrics.metric_scope', lambda x: x).start()

from aws_weather.get_met_data import app


class TestUUT(TestCase):

    def test_response_lambda_handler(self):
        from aws_weather.get_met_data import app

        ret = app.lambda_handler({}, "", mock.MagicMock())
        data = json.loads(ret["body"])

        assert ret["statusCode"] == 200
        assert "message" in ret["body"]
        assert data["message"] == "OK"

    def test_metrics_calls(self):
        context = {}
        number_of_metrics = len(app.met_metrics)
        mymock = mock.Mock()
        app.lambda_handler(event={}, context=context, metrics=mymock)
        assert mymock.put_metric.call_count == number_of_metrics
