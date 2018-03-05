from uuid import uuid4
import logging
import time

from chalice import Chalice
import boto3
from boto3.dynamodb.conditions import Key # pylint: disable=unused-import
from pythonjsonlogger import jsonlogger

#APP ENVIRONMENTAL VARIABLES
REGION = "us-east-1"
APP = "nlp-api"
NLP_TABLE = "nlp-table"

#intialize logging                                                               
log = logging.getLogger("nlp-api")                                                 
LOGHANDLER = logging.StreamHandler()                                             
FORMMATTER = jsonlogger.JsonFormatter()                                          
LOGHANDLER.setFormatter(FORMMATTER)                                              
log.addHandler(LOGHANDLER)
log.setLevel(logging.INFO)                                                       

app = Chalice(app_name='nlp-api')
app.debug = True

def dynamodb_client():
    """Create Dynamodb Client"""

    extra_msg = {"region_name": REGION, "aws_service": "dynamodb"}
    client = boto3.client('dynamodb', region_name=REGION)
    log.info("dynamodb CLIENT connection initiated", extra=extra_msg)
    return client

def dynamodb_resource():
    """Create Dynamodb Resource"""

    extra_msg = {"region_name": REGION, "aws_service": "dynamodb"}
    resource = boto3.resource('dynamodb', region_name=REGION)
    log.info("dynamodb RESOURCE connection initiated", extra=extra_msg)
    return resource

def create_nlp_record(score):
    """Creates nlp Table Record

    """

    db = dynamodb_resource()
    pd_table = db.Table(NLP_TABLE)
    guid = str(uuid4())
    res = pd_table.put_item(
        Item={
            'guid': guid,
            'UpdateTime' : time.asctime(),
            'nlp-score': score
        }
    )
    extra_msg = {"region_name": REGION, "aws_service": "dynamodb"}
    log.info(f"Created NLP Record with result{res}", extra=extra_msg)
    return guid

def query_nlp_record():
    """Scans nlp table and retrieves all records"""
    
    db = dynamodb_resource()
    extra_msg = {"region_name": REGION, "aws_service": "dynamodb", 
        "nlp_table":NLP_TABLE}
    log.info(f"Table Scan of NLPtable", extra=extra_msg)
    pd_table = db.Table(NLP_TABLE)
    res = pd_table.scan()
    records = res['Items']
    return records

@app.route('/')
def index():
    """Default Route"""
    
    return {'hello': 'world'}

@app.route("/nlp/list")
def nlp_list():
    """list nlp scores"""

    extra_msg = {"region_name": REGION, 
        "aws_service": "dynamodb", 
        "route":"/nlp/list"}
    log.info(f"List NLP Records via route", extra=extra_msg)    
    res = query_nlp_record()
    return res 
