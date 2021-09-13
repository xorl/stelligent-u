import boto3
import argparse
from os import lseek, path
from configparser import ConfigParser


creds_file = path.join(path.expanduser("~"),'.aws/credentials')
parser = argparse.ArgumentParser()
parser.add_argument("token")
parser.add_argument("username")
args = parser.parse_args()


client = boto3.client('sts')
config = ConfigParser()
config.read([creds_file])

response = client.get_session_token(
        SerialNumber=f'arn:aws:iam::324320755747:mfa/{args.username}',
        TokenCode=f'{args.token}'
    )

aki = response['Credentials']['AccessKeyId']
sak = response['Credentials']['SecretAccessKey']

print(f"KEY ID: {aki}\nSECRET KEY:{sak}")

if 'Credentials' in response:
    config.add_section('temp')
    config.set('temp','aws_access_key_id', aki)
    config.set('temp','aws_secret_access_key', sak)
    with open(creds_file, 'w') as configfile:
        config.write(configfile)
    print("Saved temp Credentials")