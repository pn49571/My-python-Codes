# /usr/bin/python2.7
# written by Tomas (www.lisenet.com) on 05/11/2012
# copyleft free software

import boto.ec2
import sys
from pprint import pprint

# specify AWS keys
auth = {"aws_access_key_id": "AKIAJ6KTPE7PQGFDCJPQ", "aws_secret_access_key": "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"}


def main(command):
    # read arguments from the command line and
    # check whether at least two elements were entered
    # if len(sys.argv) < 2:
    #     print "Usage: python aws.py {start|stop}\n"
    #     sys.exit(0)
    # else:
    #     action = sys.argv[1]
    action = command
    if action == "start":
        startInstance()
    elif action == "stop":
        stopInstance()
    elif action == "status":
        statusInstance()
    else:
        print "Usage: python aws.py {start|stop}\n"


def startInstance():
    print "Starting the instance..."

    # change "eu-west-1" region if different
    try:
        ec2 = boto.ec2.connect_to_region("us-east-1", **auth)

    except Exception, e1:
        error1 = "Error1: %s" % str(e1)
        print(error1)
        sys.exit(0)

    # change instance ID appropriately
    try:
        ec2.start_instances(instance_ids="i-0bf9ca111c5e5dc7c")

    except Exception, e2:
        error2 = "Error2: %s" % str(e2)
        print(error2)
        sys.exit(0)


def stopInstance():
    print "Stopping the instance..."

    try:
        ec2 = boto.ec2.connect_to_region("us-east-1", **auth)

    except Exception, e1:
        error1 = "Error1: %s" % str(e1)
        print(error1)
        sys.exit(0)

    try:
        ec2.stop_instances(instance_ids="i-0bf9ca111c5e5dc7c")

    except Exception, e2:
        error2 = "Error2: %s" % str(e2)
        print(error2)
        sys.exit(0)


def statusInstance():
        try:
            ec2 = boto.ec2.connect_to_region("us-east-1", **auth)

        except Exception, e1:
            error1 = "Error1: %s" % str(e1)
            print(error1)
            sys.exit(0)

        try:
            existing_instances = ec2.get_all_instances()
            print 'Listing instances'
            instances = [i for r in existing_instances for i in r.instances]
            for i in instances:
                pprint("instance Name {} and its status {}".format(i.__dict__['id'],i.__dict__['_state']))
        except Exception, e2:
            error2 = "Error2: %s" % str(e2)
            print(error2)
            sys.exit(0)


if __name__ == '__main__':
    main("status")
