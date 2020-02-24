# AWS-Web-API
Web API server built by Flora.

### Functions:
1. Web API that will accept a parameter from user and trigger a Lambda function to download the web content as an object in the block storage (Amazon S3). 
2. AWS EC2 to run a virtual machine instance that is constantly running in the back-end to monitor the object storage in S3 and generate hash values for each new page registered.

### Cloud Platform

AWS

### Platform Version

 Mac OS

### How to run command line:

in a terminal window, paste the following command line and run.

    curl -d '"[http://courses.cse.tamu.edu/chiache/csce678/s20/slides/intro.pdf](http://courses.cse.tamu.edu/chiache/csce678/s20/slides/intro.pdf)"' -H "Content-Type: application/string" -X POST [https://05pt77a6b2.execute-api.us-west-2.amazonaws.com/FloraStage](https://05pt77a6b2.execute-api.us-west-2.amazonaws.com/FloraStage)

- **PLEASE** replace `"http://courses.cse.tamu.edu/chiache/csce678/s20/slides/intro.pdf"` to a **String** of the webpage URL you want to download.

    For example: `"http://courses.cse.tamu.edu/chiache/csce678/s20/slides/virtualization.pdf"`

### s3 bucket name

yijunzhang678

### URL of AWS Lambda API Gateway

[https://05pt77a6b2.execute-api.us-west-2.amazonaws.com/FloraStage](https://05pt77a6b2.execute-api.us-west-2.amazonaws.com/FloraStage)

### Public DNS of EC2 instance

[ec2-18-236-68-24.us-west-2.compute.amazonaws.com](http://ec2-18-236-68-24.us-west-2.compute.amazonaws.com/)
