from constructs import Construct
from aws_cdk import Stack, pipelines
import aws_cdk as cdk


class CdkPipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        pipeline = pipelines.CodePipeline(
            self,
            "CdkPipeline",
            pipeline_name="CdkTaskPipeline",

            synth=pipelines.ShellStep(
                "Synth",
                input=pipelines.CodePipelineSource.connection(
                    "HARESHWARAN-S/terraform-training-26-day5",
                    "main",
                    connection_arn="arn:aws:sts::590852515231:assumed-role/AWSReservedSSO_Restricted-limited-admin_bb3e50c5ab177522/hareshwarans@presidio.com"
                ),
                commands=[
                    "npm install -g aws-cdk",
                    "python -m pip install -r requirements.txt",
                    "cdk synth"
                ]
            )
        )

        pipeline.add_stage(
            CdkTaskStage(
                self,
                "DeployStage",
                env=cdk.Environment(
                    account=self.account,
                    region=self.region
                )
            )
        )


class CdkTaskStage(cdk.Stage):

    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        from cdk_task.cdk_task_stack import CdkTaskStack

        CdkTaskStack(self, "CdkTaskStack")
