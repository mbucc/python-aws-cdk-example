```
# cdk deploy --profile research

✨  Synthesis time: 4.31s

Stack undefined
This deployment will make potentially sensitive changes according to your current security approval level (--require-approval broadening).
Please confirm you intend to make the following modifications:

IAM Statement Changes
┌───┬──────────────────────────────────────┬────────┬───────────────────────┬──────────────────────────────────────┬───────────────────────────────────────┐
│   │ Resource                             │ Effect │ Action                │ Principal                            │ Condition                             │
├───┼──────────────────────────────────────┼────────┼───────────────────────┼──────────────────────────────────────┼───────────────────────────────────────┤
│ + │ ${EventBridgeHandler.Arn}            │ Allow  │ lambda:InvokeFunction │ Service:events.amazonaws.com         │ "ArnLike": {                          │
│   │                                      │        │                       │                                      │   "AWS:SourceArn": "${EventRule.Arn}" │
│   │                                      │        │                       │                                      │ }                                     │
├───┼──────────────────────────────────────┼────────┼───────────────────────┼──────────────────────────────────────┼───────────────────────────────────────┤
│ + │ ${EventBridgeHandler/ServiceRole.Arn │ Allow  │ sts:AssumeRole        │ Service:lambda.amazonaws.com         │                                       │
│   │ }                                    │        │                       │                                      │                                       │
└───┴──────────────────────────────────────┴────────┴───────────────────────┴──────────────────────────────────────┴───────────────────────────────────────┘
IAM Policy Changes
┌───┬───────────────────────────────────┬────────────────────────────────────────────────────────────────────────────────┐
│   │ Resource                          │ Managed Policy ARN                                                             │
├───┼───────────────────────────────────┼────────────────────────────────────────────────────────────────────────────────┤
│ + │ ${EventBridgeHandler/ServiceRole} │ arn:${AWS::Partition}:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole │
└───┴───────────────────────────────────┴────────────────────────────────────────────────────────────────────────────────┘
(NOTE: There may be security-related changes not in this list. See https://github.com/aws/aws-cdk/issues/1299)

Do you wish to deploy these changes (y/n)? y
EventBridgeLambdaStack: deploying... [1/1]
EventBridgeLambdaStack: creating CloudFormation changeset...
EventBridgeLambdaStack | 0/6 | 7:29:30 AM | REVIEW_IN_PROGRESS   | AWS::CloudFormation::Stack | EventBridgeLambdaStack User Initiated
EventBridgeLambdaStack | 0/6 | 7:29:36 AM | CREATE_IN_PROGRESS   | AWS::CloudFormation::Stack | EventBridgeLambdaStack User Initiated
EventBridgeLambdaStack | 0/6 | 7:29:38 AM | CREATE_IN_PROGRESS   | AWS::IAM::Role          | EventBridgeHandler/ServiceRole (EventBridgeHandlerServiceRole70EBCB5A) 
EventBridgeLambdaStack | 0/6 | 7:29:38 AM | CREATE_IN_PROGRESS   | AWS::CDK::Metadata      | CDKMetadata/Default (CDKMetadata) 
EventBridgeLambdaStack | 0/6 | 7:29:39 AM | CREATE_IN_PROGRESS   | AWS::IAM::Role          | EventBridgeHandler/ServiceRole (EventBridgeHandlerServiceRole70EBCB5A) Resource creation Initiated
EventBridgeLambdaStack | 0/6 | 7:29:39 AM | CREATE_IN_PROGRESS   | AWS::CDK::Metadata      | CDKMetadata/Default (CDKMetadata) Resource creation Initiated
EventBridgeLambdaStack | 1/6 | 7:29:39 AM | CREATE_COMPLETE      | AWS::CDK::Metadata      | CDKMetadata/Default (CDKMetadata) 
EventBridgeLambdaStack | 2/6 | 7:29:55 AM | CREATE_COMPLETE      | AWS::IAM::Role          | EventBridgeHandler/ServiceRole (EventBridgeHandlerServiceRole70EBCB5A) 
EventBridgeLambdaStack | 2/6 | 7:29:56 AM | CREATE_IN_PROGRESS   | AWS::Lambda::Function   | EventBridgeHandler (EventBridgeHandlerBDEBA77F) 
EventBridgeLambdaStack | 2/6 | 7:29:58 AM | CREATE_IN_PROGRESS   | AWS::Lambda::Function   | EventBridgeHandler (EventBridgeHandlerBDEBA77F) Resource creation Initiated
EventBridgeLambdaStack | 2/6 | 7:29:59 AM | CREATE_IN_PROGRESS   | AWS::Lambda::Function   | EventBridgeHandler (EventBridgeHandlerBDEBA77F) Eventual consistency check initiated
EventBridgeLambdaStack | 2/6 | 7:29:59 AM | CREATE_IN_PROGRESS   | AWS::Events::Rule       | EventRule (EventRule5A491D2C) 
EventBridgeLambdaStack | 2/6 | 7:30:00 AM | CREATE_IN_PROGRESS   | AWS::Events::Rule       | EventRule (EventRule5A491D2C) Resource creation Initiated
EventBridgeLambdaStack | 3/6 | 7:30:04 AM | CREATE_COMPLETE      | AWS::Lambda::Function   | EventBridgeHandler (EventBridgeHandlerBDEBA77F) 
3/6 Currently in progress: EventBridgeLambdaStack, EventRule5A491D2C
EventBridgeLambdaStack | 3/6 | 7:30:50 AM | CREATE_IN_PROGRESS   | AWS::Events::Rule       | EventRule (EventRule5A491D2C) Eventual consistency check initiated
EventBridgeLambdaStack | 3/6 | 7:30:51 AM | CREATE_IN_PROGRESS   | AWS::Lambda::Permission | EventRule/AllowEventRuleEventBridgeLambdaStackEventBridgeHandler5AFC7128 (EventRuleAllowEventRuleEventBridgeLambdaStackEventBridgeHandler5AFC7128BDB81225) 
EventBridgeLambdaStack | 3/6 | 7:30:52 AM | CREATE_IN_PROGRESS   | AWS::Lambda::Permission | EventRule/AllowEventRuleEventBridgeLambdaStackEventBridgeHandler5AFC7128 (EventRuleAllowEventRuleEventBridgeLambdaStackEventBridgeHandler5AFC7128BDB81225) Resource creation Initiated
EventBridgeLambdaStack | 4/6 | 7:30:52 AM | CREATE_COMPLETE      | AWS::Lambda::Permission | EventRule/AllowEventRuleEventBridgeLambdaStackEventBridgeHandler5AFC7128 (EventRuleAllowEventRuleEventBridgeLambdaStackEventBridgeHandler5AFC7128BDB81225) 
EventBridgeLambdaStack | 5/6 | 7:31:00 AM | CREATE_COMPLETE      | AWS::Events::Rule       | EventRule (EventRule5A491D2C) 
EventBridgeLambdaStack | 6/6 | 7:31:01 AM | CREATE_COMPLETE      | AWS::CloudFormation::Stack | EventBridgeLambdaStack 

 ✅  EventBridgeLambdaStack

✨  Deployment time: 96.91s

Stack ARN:
arn:aws:cloudformation:us-east-1:588738607782:stack/EventBridgeLambdaStack/66f7c730-b6f2-11ef-83b5-0e6883d3918d

✨  Total time: 101.22s

#
```
