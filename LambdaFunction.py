import json
import urllib.request
import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # event is input string from user
    # Calling urlopen with this Request object returns a response object for the URL requested.
    url = event
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    webContent = response.read()

    bucket_name = '***************'
    bucket_key = url
    body = webContent
    put_object_into_s3(bucket_name, bucket_key, body)

    return {
        'statusCode': 200,
        'url': url
    }

def put_object_into_s3(bucket_name, bucket_key, body):
    response = s3_client.put_object(Bucket=bucket_name, Key=bucket_key, Body=body)
    status_code = response['ResponseMetadata']['HTTPStatusCode']
