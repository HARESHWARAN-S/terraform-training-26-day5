#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_task.cdk_task_stack import CdkTaskStack

app = cdk.App()
CdkTaskStack(app, "CdkTaskStack")

app.synth()