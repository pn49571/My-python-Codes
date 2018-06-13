import boto3


s3 = boto3.client('s3')

copy_source = {
    'Bucket': 'eni.lightning',
    'Key': 'LTG/2018-06-06/Archive-2018-06-06T13-00.ltg'
}

s3.copy(
  copy_source, 'eni.lightning', 'LTG/2018-06-06/Archive-2018-06-06T13-00.ltg',
  ExtraArgs = {
    'StorageClass': 'STANDARD_IA',
    'MetadataDirective': 'COPY'
  }
)
