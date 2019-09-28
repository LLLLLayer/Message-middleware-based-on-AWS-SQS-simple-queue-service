import logging
import boto3
from botocore.exceptions import ClientError

def retrieve_sqs_messages(sqs_queue_url, num_msgs=1, wait_time=0, visibility_time=5):
    if num_msgs < 1:
        num_msgs = 1
    elif num_msgs > 10:
        num_msgs = 10
    sqs_client = boto3.client('sqs')
    try:
        msgs = sqs_client.receive_message(QueueUrl=sqs_queue_url,
                                          MaxNumberOfMessages=num_msgs,
                                          WaitTimeSeconds=wait_time,
                                          VisibilityTimeout=visibility_time
                                          )
    except ClientError as e:
        logging.error(e)
        return None
    return msgs['Messages']


def delete_sqs_message(sqs_queue_url, msg_receipt_handle):
    sqs_client = boto3.client('sqs')
    sqs_client.delete_message(QueueUrl=sqs_queue_url,
                              ReceiptHandle=msg_receipt_handle)


def receive(inputUrl, inputNum=1, inputWait=0, inputVis=5):
    if inputUrl=="default":
        sqs_queue_url = "https://sqs.us-east-1.amazonaws.com/679713548902/SAtest"
    else:
        sqs_queue_url = inputUrl

    num_messages = inputNum
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    str=""
    msgs = retrieve_sqs_messages(sqs_queue_url, num_messages,inputWait,inputVis)
    if msgs is not None:
        for msg in msgs:
            print(msg['Body'])
            str += msg['Body']
            delete_sqs_message(sqs_queue_url, msg['ReceiptHandle'])
    return str

