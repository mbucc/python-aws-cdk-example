from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_events as events,
    aws_events_targets as targets
)

class EventBridgeLambdaStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define the Lambda function
        lambda_function = _lambda.Function(
            self,
            "EventBridgeHandler",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_inline(
                """
import json

def lambda_handler(event, context):
    print("Event received:", json.dumps(event))
    return {"statusCode": 200, "body": "Event processed successfully"}
                """
            ),
        )

        # Define an EventBridge rule
        event_rule = events.Rule(
            self,
            "EventRule",
            event_pattern={
                "source": ["my.custom.source"]
            }
        )

        # Add the Lambda function as a target for the rule
        event_rule.add_target(targets.LambdaFunction(lambda_function))

app = core.App()
EventBridgeLambdaStack(app, "EventBridgeLambdaStack")
app.synth()
