import aws_cdk as cdk
from cdk_task.cdk_pipeline_stack import CdkPipelineStack

app = cdk.App()

CdkPipelineStack(
    app,
    "CdkPipelineStack",
    env=cdk.Environment(
        account="590852515231",
        region="us-east-1"
    )
)

app.synth()
