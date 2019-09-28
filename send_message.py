import logging
import boto3
from botocore.exceptions import ClientError

sqs_queue_url="https://sqs.us-east-1.amazonaws.com/679713548902/SAtest"

def send_sqs_message(sqs_queue_url, msg_body):
    sqs_client = boto3.client('sqs')
    try:
        msg = sqs_client.send_message(QueueUrl=sqs_queue_url,
                                      MessageBody=msg_body)
    except ClientError as e:
        logging.error(e)
        return None
    return msg


def send(inputUrl,inputMessage):
    if inputUrl == "default":
        sqs_queue_url = "https://sqs.us-east-1.amazonaws.com/679713548902/SAtest"
    else:
        sqs_queue_url = inputUrl
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')
    for i in range(1, 2):
        msg_body = f'SQS message #{i}'
        msg = send_sqs_message(sqs_queue_url, inputMessage)
        if msg is not None:
            logging.info(f'Sent SQS message ID: {msg["MessageId"]}')