import json
import logging
import boto3
from crhelper import CfnResource
import params

logger = logging.getLogger(__name__)
helper = CfnResource(
    json_logging=False,
    log_level="DEBUG",
    boto_level="CRITICAL",
    sleep_on_delete=120,
    ssl_verify=None,
)

@helper.create
@helper.update
def parse_config(event, _):
    raw_params = event["ResourceProperties"]["MainStackParams"]
    params_dict = Params.get_dict_from_params_input_agnostic(raw_params)
    helper.Data.update(**params_dict)
    return None

@helper.delete
def no_op(_, __):
    return None

def handler(event, context):
    helper(event, context)