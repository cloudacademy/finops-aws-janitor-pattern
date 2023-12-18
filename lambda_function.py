import boto3
import logging

ec2 = boto3.resource('ec2')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("identifying unattached volumes...")

    vol_filter = [
        {'Name':'tag:AutoDelete', 'Values':['True']},
        {'Name': 'status','Values': ['available']}
    ]

    volumes = [v for v in ec2.volumes.filter(Filters=vol_filter)]

    logger.info(f"volumes unattached: {volumes}")

    for vol in volumes:
        logger.info(f"deleting volume: {vol.id}")
        vol.delete()

    logger.info("unattached volumes deleted")