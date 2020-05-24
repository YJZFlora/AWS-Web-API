# AWS Web API

## Functions achieve

* Built a web API that will accept a parameter from user and trigger a Lambda function to download the web content as an object in the block storage (Amazon S3).
* Used AWS EC2 to run a virtual machine instance that is constantly running in the back-end to monitor the object storage in S3 and generate hash values for each new page registered.

## Techniques

AWS Lambda Function, AWS API Gateway, AWS S3, AWS EC2, AWS SQS, Python

## How to achieve

![Image of architecture](https://github.com/YJZFlora/AWS-Web-API/blob/master/Architecture.png)

## Problem and solution

**Problem:**  JSON Object cannot be sent to API Gateway. " CORS header 'Access-Control-Allow-Origin' missing" error.

**Solution:**  Enable CORS in AWS API Gateway. 'Access-Control-Allow-Headers' should use the ```*``` wildcard.

**Problem:**  Running instance in EC2 could charge fees.

**Solution:**  Shut down EC2 when unneeded.

## Future work

* Make a front-end for user to input query.

## References

https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-getting-started-with-rest-apis.html

https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS/Errors/CORSMissingAllowOrigin

http://courses.cse.tamu.edu/chiache/csce678/s20/project1.html
