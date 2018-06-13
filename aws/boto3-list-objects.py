import boto3

s3_client = boto3.client('s3')
bucket = 'eni.lightning'
prefix = 'GlmFusion/2018/'

# response = s3_client.list_objects(
#     Bucket = bucket,
#     Prefix = prefix
# )

s3 = boto3.resource('s3')
my_bucket = s3.Bucket('eni.lightning')

for object_summary in my_bucket.objects.filter(Prefix=prefix):
    print(object_summary.key)
    copy_source = {
        'Bucket': 'eni.lightning',
        'Key': object_summary.key
    }
    s3_client.copy(
      copy_source, 'eni.lightning', object_summary.key,
      ExtraArgs = {
          'StorageClass': 'STANDARD_IA',
          'MetadataDirective': 'COPY'
      }
    )
# for file in response['Contents']:
#     print(file['Key'])
