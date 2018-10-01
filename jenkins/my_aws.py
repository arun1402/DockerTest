# /usr/bin/python2.7
# written by Tomas (www.lisenet.com) on 05/11/2012
# copyleft free software

import boto.ec2
import sys

# specify AWS keys
auth = {"aws_access_key_id": "AKIAIY6Y5DFPQIM7WDWA", "aws_secret_access_key": "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"}

def main():
	monitorInstance()		

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
        ec2.start_instances(instance_ids=["i-04bdbf45351ca64d4","i-0ec9f6f4b793c76c1"])
		 
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
        ec2.stop_instances(instance_ids=["i-04bdbf45351ca64d4","i-0ec9f6f4b793c76c1"])
		
    except Exception, e2:
        error2 = "Error2: %s" % str(e2)
        print(error2)
        sys.exit(0)
		
def monitorInstance():
	print "Monitoring the instance status..."
	
	try:
		ec2 = boto.ec2.connect_to_region("us-east-1", **auth)

    except Exception, e1:
        error1 = "Error1: %s" % str(e1)
        print(error1)
        sys.exit(0)
	
	try:
        ec2.instancestatus(instance_ids=["i-04bdbf45351ca64d4","i-0ec9f6f4b793c76c1"])
	
	except Exception, e2:
        error2 = "Error2: %s" % str(e2)
        print(error2)
        sys.exit(0)
		
if __name__ == '__main__':
    main()