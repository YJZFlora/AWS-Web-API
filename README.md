# AWS Web API

## Functions achieve

* Built a web API that will accept a parameter from user and trigger a Lambda function to download the web content as an object in the block storage (Amazon S3).
* Used AWS EC2 to run a virtual machine instance that is constantly running in the back-end to monitor the object storage in S3 and generate hash values for each new page registered.

## Techniques

AWS Lambda Function, AWS API Gateway, AWS S3, AWS EC2, Python

## How to achieve

1. Query -> API -> Lambda Function
![Image of api](https://github.com/YJZFlora/AWS-Web-API/blob/master/api_architecture.png)

2. EC2 monitoring


## Demo

## Problem and solution

**Problem** JSON Object cannot be sent to API Gateway. " CORS header 'Access-Control-Allow-Origin' missing" error.

**Solution** Enable CORS in AWS API Gateway. 'Access-Control-Allow-Headers' should use the ```*``` wildcard.

## Future work

* Make a front-end for user to input query.


## References

https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-getting-started-with-rest-apis.html

https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS/Errors/CORSMissingAllowOrigin


如何写Readme的内容：
目的：描述一下为什么做这个项目？好玩（interest，passion）？学习某个知识点？
‍‌‍‍‌‍‌‌‍‍‍‍‍‌‍‌‌‌‍keyword：涉及的技术知识点
描述一下整个项目的架构
描述一下有哪些功能
demo video
遇到的问题，怎么解决的
未解决的问题future work
参考资料链接
license
