#!/usr/bin/env python

import click
import boto3

@click.command()
@click.option('-create', help='Create stack', is_flag=True)
@click.option('-desc',
            help='Describe Stack', is_flag=True)
@click.option('-update', help='Update stack name', is_flag=True)
@click.option('-protect', help='Disable or Enable protection on a stack', is_flag=True)
@click.option('-name', required=True, help='Bucket name')
def main(create, desc, update, protect, name):
    print("Stack tool for Lab 1")
    if create:
        print(f"We're creating the stack {stack}")
        s3 = boto3.resource('s3')
         s3.create_bucket(Bucket=f'{name}')


if __name__ == "__main__":
    main()