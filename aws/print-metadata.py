
import boto
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from boto.s3.connection import OrdinaryCallingFormat


def print_key_metadata(bucket_name, key_name):
    c = boto.connect_s3(aws_access_key_id = 'AKIAJ6KTPE7PQGFDCJPQ',
                        aws_secret_access_key = '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',
                        calling_format=OrdinaryCallingFormat())
    # for bucket in c.get_all_buckets():
    #     print(bucket)
    #     if bucket.name == 'eni.lightning':
    #         for key in bucket.list():
    #             print "{name}\t{size}\t{modified}".format(
    #                     name = key.name,
    #                     size = key.size,
    #                     modified = key.last_modified,
    #                     )
        # print "{name}\t{created}".format(
        #         name = bucket.name,
        #         created = bucket.creation_date,
        # )
    b = c.get_bucket("eni.lightning")
    k = Key(b)
    k.key = 'python_api_sample_code_py.txt'
    print(k.change_storage_class('STANDARD_IA'))
    # for key in b.list():



print_key_metadata("eni.lightning","app_password.txt")
