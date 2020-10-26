#!/usr/bin/env python
# coding: utf-8

#%%
#pip install boto3


#%%
import boto3


#%%
s3 = boto3.resource('s3')


#%%

for bucket in s3.buckets.all():
    print(bucket.name)


#%%
'''
# Create my second bucket
response = s3.create_bucket(Bucket='cseng-1374-tuxedo',
                            CreateBucketConfiguration={
                                    'LocationConstraint': 'eu-central-1'},)

# Print out the response
print(response)
'''


#%% check, if new bucket is in the list
for bucket in s3.buckets.all():
    print(bucket.name)



#%%

# get the client first
s3_client = s3.meta.client


#%%

bucket_list = s3_client.list_buckets()

# Iterate over Buckets from .list_buckets() response
for bucket in bucket_list['Buckets']:
  
    # Print the Name for each bucket
    print(bucket['Name'])


#%%
# delete the first bucket created with EC2 instance
#s3_client.delete_bucket(Bucket='cseng-1374')

#%%

