import pymysql
import json
import boto3
from botocore.exceptions import ClientError
ses=boto3.client('ses')
SENDER=""

def send_emails(name, email):
    try:
       res = ses.send_templated_email(
           Source=SENDER,
           Destination={
           'ToAddresses': [str(email)],
        },
        Template='Keepsl_welcome_Template',
        TemplateData="{\"user\":\""+str(name)+"\"}"
    )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
      print("Email sent! Message ID:",res['MessageId']),

    return

def lambda_handler(event, context):
    name=event['multiValueHeaders']['name']
    names=str(name[0])
    email=event['multiValueHeaders']['email']
    emails=str(email[0])
    send_emails(names,emails)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully sent mail from AWS Lambda!')
        }
    
