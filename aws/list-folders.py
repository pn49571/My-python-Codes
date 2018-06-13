import boto3

s3 = boto3.resource('s3')
bucket = 'eni.lightning'
prefix = 'GlmFusion/2018/'
b = s3.Bucket('eni.lightning')

result = b.meta.client.list_objects(Bucket=b.name, Prefix=prefix,
                                         Delimiter='/')
for o in result.get('CommonPrefixes'):
    print(o.get('Prefix'))
