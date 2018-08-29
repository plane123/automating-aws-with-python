# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print(bucket)
    
get_ipython().run_line_magic('pwd', '')
aws s3 mb s3://automatingawsptlane-commandline
new_bucket = s3.create_bucket(Bucket='automatingawsptlane-boto3')
for bucket in s3.buckets.all():
    print(bucket)
    
ec2_client = session.client('ec2')
get_ipython().run_line_magic('history', '')
