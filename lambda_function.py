import boto3
import logging

ec2 = boto3.client('ec2')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# sns_client = boto3.client('sns')
volumes = ec2.describe_volumes()

def lambda_handler(event, context):
    unused_volumes = []
    for vol in volumes['Volumes']:
        if len(vol['Attachments']) == 0:
            vol1 = ("-----Unused Volume ID = {}------".format(vol['VolumeId']))
            unused_volumes.append(vol1)
    
    #email
    # sns_client.publish(
    #     TopicArn='<SNS Topic ARN>',
    #     Subject='Warning - Unused Volume List',
    #     Message=str(unused_volumes)
    # )

    print("EBS vols to delete:")
    for vol in unused_volumes:
        print(vol)

    return {
        "statusCode": 200,
        "isBase64Encoded": False,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": {"unused_volumes": unused_volumes}
    }