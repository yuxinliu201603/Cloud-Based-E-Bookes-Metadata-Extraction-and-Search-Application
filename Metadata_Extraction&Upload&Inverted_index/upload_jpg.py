
# coding: utf-8

# In[26]:


from google.cloud import storage
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/yuxinliu/Downloads/inf551project-e3352f07f6b3.json"
# Enable Storage
client = storage.Client()
#path = 'dataSet'

# Reference an existing bucket.
bucket = client.get_bucket('inf551project-c1290.appspot.com')



os.chdir('/Users/yuxinliu/INF551_project/')
a = os.listdir('Engineering')
a.remove('.ipynb_checkpoints')
os.chdir('Engineering')
print (os.getcwd())
print(a)
for i in a:
    upload_jpg(i)


# In[25]:


def upload_jpg(name):
    zebraBlob = bucket.blob(name)
    zebraBlob.upload_from_filename(name)
    a = zebraBlob.path
    print(a)


# In[20]:


https://firebasestorage.googleapis.com/v0/b/inf551project-c1290.appspot.com/o/Chemical%20Engineering%20Vocabulary.pdf?alt=media&token=6bb60979-fb0a-4e10-93ef-520b3c064bef
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    #"""Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))


# In[ ]:


def upload_pdf(name):
    blob = bucket.get_blob('remote/path/to/file.txt')
    print(blob.download_as_string())
    blob.upload_from_string('New contents!')
    blob2 = bucket.blob('remote/path/storage.txt')
    blob2.upload_from_filename(filename='/Users/yuxinliu/INF551_project/Accounting/%s'%i)

