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

file_path = '../chris/Documents/Python Notebooks/Projects/GraphRecommender/netflix_titles.csv'

# Upload final_report.csv with key 2019/final_report_01_01.csv
s3_client.upload_file(Bucket='cseng-1374-tuxedo', 
               # Set filename and key
               Filename=file_path, 
               Key='Q1374/netflix_tiles.csv')

# Get object metadata and print it
response = s3_client.head_object(Bucket='cseng-1374-tuxedo', 
                       Key='Q1374/netflix_tiles.csv')

# Print the size of the uploaded object
print(response['ContentLength'])

#%%
def del_by_filename(bucket, filename):
    # get key referred by filename
    object_summary = s3.ObjectSummary(bucket,filename)
    print(object_summary)
    #s3.Object('cseng-1374-tuxedo', 'Q1374/netflix_tiles.csv').delete()

#%%
del_by_filename('cseng-1374-tuxedo', file_path)
