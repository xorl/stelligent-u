#!/usr/local/bin/bash
###################################

###################################
# Create buckets in the specific 
# regions.
#  
###################################

STACK_NAME="ryan.lewon.labs"
REGIONS=("us-west-2" "us-east-2" "us-east-1" "us-west-1")
TEMP_BODY=ryan.lewon.labs.yml
PARAM_FILE=ryan.lewon.labs.json

for i in $REGIONS;
do
    echo "Creating stack in region $i";
    aws cloudformation create-stack --stack-name $STACK_NAME --template-body file://$TEMP_BODY --parameters file://$PARAM_FILE --region "$i" | jq
    echo "Created stack in region $i";
done