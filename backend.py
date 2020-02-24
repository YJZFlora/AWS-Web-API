import boto3
import json
import botocore
import hashlib
client = boto3.client(
    's3',
    aws_access_key_id = "AKIAWTHXAOKAUNXDEG5Y",
    aws_secret_access_key = "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"
)

BUCKET_NAME = 'yijunzhang678'

flora_session = boto3.Session(region_name='us-west-2',aws_access_key_id = "AKIAWTHXAOKAUNXDEG5Y",aws_secret_access_key = "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",)
sqs = flora_session.resource('sqs')
queue = sqs.get_queue_by_name(QueueName = 's3event')
for message in queue.receive_messages():
    parsed_json = (json.loads(message.body))
    key = parsed_json['Records'][0]['s3']['object']['key']
    print(key)
    if(key == ""):
        message.delete()
    else:
  key = key.replace("%3A", ":")
        #now we check if the item is a hashed item. Ignore it if it's
        if(key.find("/hash")==-1):
            # Hash
            hashedKey = key+"/hash"
            try:
                item = client.head_object(Bucket = BUCKET_NAME, Key = hashedKey)
            except botocore.exceptions.ClientError as exc:
                # hash the new one
                obj = client.get_object(Bucket = BUCKET_NAME, Key = key)
                raw_content = obj['Body'].read()
                hashed_content = hashlib.sha256(raw_content).hexdigest()
                # upload the object to S3
                s3_response = client.put_object(Bucket=BUCKET_NAME, Key=hashedKey, Body = hashed_content)
                print("hashedKey: " + hashedKey)
                print("BUCKET_NAME: " +BUCKET_NAME)
    message.delete()
