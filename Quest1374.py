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

# or alternatively
#s3_client = boto3.client('s3')

#%%

bucket_list = s3_client.list_buckets()

# Iterate over Buckets from .list_buckets() response
for bucket in bucket_list['Buckets']:
  
    # Print the Name for each bucket
    print(bucket['Name'])



#%%

file_path1 = '../chris/Documents/Python Notebooks/Projects/GraphRecommender/netflix_titles.csv'
file_path2 = '../chris/Documents/Python Notebooks/Projects/FireProject/disaster_tweets.csv'
file_list = [file_path1, file_path2]
bucket = 'cseng-1374-tuxedo'

# Upload final_report.csv with key 2019/final_report_01_01.csv

for file in file_list:
    file_key = 'Q1374/' + str(str.split(file, '/')[-1])

    s3_client.upload_file(Bucket=bucket, 
               # Set filename and key
               Filename=file, 
               Key=file_key)

# Get object metadata and print it
#response = s3_client.head_object(Bucket='cseng-1374-tuxedo', 
#                       Key='Q1374/netflix_tiles.csv')

# Print the size of the uploaded object
#print(response['ContentLength'])


#%%
def del_by_filename(bucket, filename):
    response = s3.Object(bucket, filename).delete()
    print(response)

#%%
del_by_filename(bucket, 'Q1374/netflix_titles.csv')






