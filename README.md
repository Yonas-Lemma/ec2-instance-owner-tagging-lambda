# EC2 Instance Owner Tagging Lambda

## Overview

This AWS Lambda function automatically tags newly created EC2 instances with the username of the IAM user who launched the instance. It listens to EC2 instance launch events and applies an `Owner` tag to the instance, helping teams track resource ownership and improve cloud resource management.

**How this helps:**  
Whenever an EC2 instance is launched, this solution captures the launch event using **AWS EventBridge** (which listens to CloudTrail events), triggers the Lambda function, and tags the instance with the username of the person who launched it. This makes it easy to identify who launched each instance, improving accountability and operational transparency.

---

## Features

- Extracts the IAM username from the CloudTrail event triggering the Lambda.
- Tags the EC2 instance with the key `Owner` and the username as the value.
- Supports multi-instance launches by tagging the first instance in the event.
- Simple and lightweight Python implementation using Boto3.

---

## How It Works

1. The Lambda function is triggered by an AWS **EventBridge** rule that listens for EC2 instance launch events recorded by **CloudTrail**.
2. The function extracts the username and instance ID from the event payload.
3. It calls the EC2 `create_tags` API to add an `Owner` tag to the instance.

---

## Prerequisites

- AWS account with permissions to create Lambda functions and EventBridge rules.
- IAM role for the Lambda with permissions:
  - `ec2:CreateTags`
  - `logs:CreateLogGroup`
  - `logs:CreateLogStream`
  - `logs:PutLogEvents`

---

## Deployment Steps

1. Create an IAM role with the necessary permissions for the Lambda function.
2. Create the Lambda function using the provided Python code.
3. Create an EventBridge rule to trigger the Lambda on EC2 instance launch events:
   - Event pattern example:
     ```json
     {
       "source": ["aws.ec2"],
       "detail-type": ["AWS API Call via CloudTrail"],
       "detail": {
         "eventName": ["RunInstances"]
       }
     }
     ```
4. Attach the Lambda function as the target of the EventBridge rule.
