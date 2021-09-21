#!/usr/bin/env python

import click
import boto3

@click.command()
@click.option('-create', help='Create stack', is_flag=True)
@click.option('-desc',
            help='Describe Stack', is_flag=True)
@click.option('-update', help='Update stack name', is_flag=True)
@click.option('-protect', help='Disable or Enable protection on a stack', is_flag=True)
@click.option('-stack', required=True, help='Stack name')
def main(create, desc, update, protect, stack):
    print("Stack tool for Lab 1")
    if create:
        print(f"We're creating the stack {stack}")


if __name__ == "__main__":
    main()