# Simple AWS Greengrass Lambda function to publish a response message to AWS IoT Cloud
# Part of Lab 18
# Make sure your subscription routes traffic from this Lambda to the /ratchet-cloud topic

import sys
import logging
import json
import greengrasssdk

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

client = greengrasssdk.client('iot-data')

def Ratchet_Hello_handler(event, context):
    logger.info("Ratchet Lambda is ONLINE")
    logger.info(json.dumps(event))

    # Let's publish a response back to AWS IoT
    client.publish(topic = "/ratchet-cloud", payload = json.dumps(event))

    return True
