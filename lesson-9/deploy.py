import boto3

ec2 = boto3.resource('ec2', region_name='us-east-1')
filters = [
    {'Name': 'tag:proj', 'Values': ['*hillel-lesson*']},
    {'Name': 'tag:env', 'Values': ['*dev*']}
]

response = ec2.instances.filter(Filters=filters)

for instance in response:
    print(instance.public_ip_adress)
