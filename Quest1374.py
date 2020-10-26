#!/usr/bin/env python
# coding: utf-8

# In[2]:


#pip install boto3


# In[3]:


import boto3


# In[5]:


s3 = boto3.resource('s3')


# In[6]:


for bucket in s3.buckets.all():
    print(bucket.name)


# In[8]:

'''
# Create my second bucket
response = s3.create_bucket(Bucket='cseng-1374-tuxedo',
                            CreateBucketConfiguration={
                                    'LocationConstraint': 'eu-central-1'},)

# Print out the response
print(response)
'''

# In[9]:


# check, if new bucket is in the list
for bucket in s3.buckets.all():
    print(bucket.name)



# In[15]:


# Get the list_buckets response

# # the following did not work, as s3 was the resource and not the client 
#response = s3.list_buckets()

# so get the client first
s3_client = s3.meta.client


# In[16]:


bucket_list = s3_client.list_buckets()

# Iterate over Buckets from .list_buckets() response
for bucket in bucket_list['Buckets']:
  
    # Print the Name for each bucket
    print(bucket['Name'])


# In[19]:
# delete the first bucket created with EC2 instance
#s3_client.delete_bucket(Bucket='cseng-1374')

#%%

