December 10, 2024

Python CDK Example
==============================

Creates a Lambda that listens for an EventBridge event.

This could be used for a bridge that is triggered on a timer
for example.


Setup
------------------

    npm install -g aws-cdk
    cdk init app --language python
    pip install aws-cdk-lib constructs



Deploy
------------------


    aws sso login --profile research
    cdk deploy --profile research


This assumes you have run `cdk bootstrap` in the account you
log in to.


Test
-----------------

    export AWS_REGION=us-east-1
    $(aws configure export-credentials --profile research --format env)
    aws events put-events --entries '[                               
      {
        "Source": "my.custom.source",
        "DetailType": "MyEvent",
        "Detail": "{\"key1\": \"value1\"}"
      }
    ]'
    {
        "FailedEntryCount": 0,
        "Entries": [
            {
                "EventId": "d173546f-f273-bbf0-6632-b4202b360da8"
            }
        ]
    }
