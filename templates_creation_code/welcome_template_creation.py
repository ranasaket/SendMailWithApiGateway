import boto3
import codecs
from botocore.exceptions import ClientError

ses=boto3.client('ses')
file = codecs.open("templates_creation_code/Reg_success.html", "r", "utf-8")
z=file.read()

response = ses.create_template(
    Template={
        'TemplateName': 'Keepsl_welcome_Template',
        'SubjectPart': 'KEEPSL Welcome',
        'HtmlPart':str(z), 

    }
)

print(response)
