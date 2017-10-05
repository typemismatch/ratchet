# Simple AWS Greengrass Lambda function to publish a messsage in response to button presses
# Part of Lab 19
# Make sure your subscription routes traffic from this Lambda to the /ratchet-lcd topic

import sys
import logging
import json
import greengrasssdk

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

client = greengrasssdk.client('iot-data')

def Ratchet_ButtonPress_handler(event, context):
    logger.info("Ratchet Button Press is ONLINE")
    logger.info(json.dumps(event))

    # Let's publish a response back to AWS IoT
    # Only send a message if the button state is 1
    if (event['key'] == 'ENTER' and event['state'] > 0):
        client.publish(topic = "/ratchet-lcd", payload = "Button Pressed")

    return True
