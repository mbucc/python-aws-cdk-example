from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_events as events,
    aws_events_targets as targets,
)
from constructs import Construct

class EventBridgeLambdaStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define the Lambda function
        lambda_function = _lambda.Function(
            self,
            "EventBridgeHandler",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset("cmd")
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

# Entry point for the CDK application
from aws_cdk import App

app = App()
EventBridgeLambdaStack(app, "EventBridgeLambdaStack")
app.synth()

